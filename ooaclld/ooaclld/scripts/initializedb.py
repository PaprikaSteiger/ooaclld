from pathlib import Path
import datetime
from collections import defaultdict

import pycldf
from tqdm import tqdm
import sqlalchemy
from urllib.parse import unquote

from clld.cliutil import Data, slug, bibtex2source, add_language_codes
from clld.db.meta import DBSession
from clld.db.models import common
from clld.lib.bibtex import Database


import ooaclld
from ooaclld import models


def main(args):

    #assert args.glottolog, 'The --glottolog option is required!'
    cldf_dir = Path(__file__).parent.parent.parent.parent / "cldf"
    # args.log.info('Loading dataset')
    ds = list(pycldf.iter_datasets(cldf_dir))[0]
    data = Data()
    data.add(
        common.Dataset,
        ooaclld.__name__,
        id=ooaclld.__name__,
        domain='ooaclld',

        publisher_name="Max Planck Institute for the Science of Human History",
        publisher_place="Jena",
        publisher_url="http://www.shh.mpg.de",
        license="http://creativecommons.org/licenses/by/4.0/",
        jsondata={
            'license_icon': 'cc-by.png',
            'license_name': 'Creative Commons Attribution 4.0 International License'},

    )
    DBSession.flush()

    for rec in tqdm(Database.from_file(ds.bibpath), desc='Processing sources'):
        ns = bibtex2source(rec, common.Source)
        data.add(common.Source, ns.id, _obj=ns)
    DBSession.flush()


    for row in tqdm(ds.iter_rows('contributors.csv'), desc="Processing contributors"):
        data.add(common.Contributor, row["ContributorID"],
                 id=row['ContributorID'],
                 name=row['Name'],
                 )
    DBSession.flush()

    for c, row in enumerate(tqdm(ds.iter_rows('featuresets.csv'), desc='Processing featuresets')):
        desc = None
        descr_path = cldf_dir / 'docs' / (row["Name"]+".html")
        if descr_path.exists():
            desc = open(descr_path).read()
        fset = data.add(models.OOAFeatureSet, row["FeatureSetID"],
                 id=row["FeatureSetID"],
                 name=row['Name'],
                 domains=row['Domain'],
                 authors=";".join(row['Authors']),
                 contributors=";".join(row['Contributors'] or [""]),
                 filename=row['Filename'] or "",
                 description=desc,
                 )
        # cnt = 0
        # for i, f in enumerate(['Authors', 'Contributors']):
        #     if row[f]:
        #         for co in row[f]:
        #             print(co)
        #             data.add(common.ContributionContributor, co,
        #                      contribution=fset,
        #                      contributor_pk=data['Contributor'][co].pk,
        #                      primary=(i == 0),
        #                      ord=cnt)
        #             cnt += 1
        DBSession.flush()

    for row in tqdm(ds.iter_rows('ParameterTable'), desc="Processing parameters"):
        data.add(models.OOAParameter, row["ParameterID"],
                 id=row["ParameterID"],
                 featureset_pk=data["OOAFeatureSet"][row["FeatureSet"]].pk,
                 featureset_name=row["FeatureSet"],
                 question=row["Question"],
                 datatype=row["datatype"],
                 visualization=row["VisualizationOnly"],
                 )
    DBSession.flush()


    all_languages = {row["LanguageID"] for row in ds.iter_rows('ValueTable')}

    for row in tqdm(ds.iter_rows('LanguageTable'), desc='Processing languages'):
        if row["Glottocode"] not in all_languages:
            continue
        data.add(models.OOALanguage, row['Glottocode'],
                 id=row['Glottocode'],
                 glottocode=row['Glottocode'],
                 name=row['Name'],
                 latitude=row['Latitude'],
                 longitude=row['Longitude'],
                 macroarea=row['Macroarea'],
                 iso=row["ISO639P3code"],
                 family_id=row["Family_ID"],
                 language_id=row["Language_ID"],
                 family_name=row["Family_Name"],
                 balanced=row["Isolates_Balanced_Sample"],
                 isolates=row["Isolates_Sample"],
                 american=row["American_Sample"],
                 world=row["Worldwide_Sample"],
                 north_america="North_America_25_Sample",
                 noun=row["Noun_Poss_Sample"],
                 )
    DBSession.flush()

    for row in tqdm(ds.iter_rows('codes.csv'), desc="Processing codes"):
        data.add(common.DomainElement, row['CodeID'].replace(".", "").replace("]", ""),
                 id=row['CodeID'].replace(".", "").replace("]", ""),
                 description=row['Description'],
                 jsondata={'Visualization': row['Visualization']},
                 parameter_pk=data['OOAParameter'][row['ParameterID'].replace(".", "")].pk)
    DBSession.flush()

    # read value table
    for row in tqdm(ds.iter_rows('ValueTable'), desc="Processing values"):
        # TODO: This is just to make the code work, ignore the second code id, see todo below for relationship modelling
        code_id = row["CodeID"].split(";")[0] if row["CodeID"] else row["CodeID"]
        data.add(models.OOAUnit, row["ID"],
                 # TODO: this would be the way to refer to another resource from a table
                 # parameter = relationship('Parameter', innerjoin=True, backref='valuesets')
                 # then accessable via self.parameter.(...)
                 id=row["ID"],
                 language_pk=data["OOALanguage"][row["LanguageID"]].pk,
                 parameter_pk=data["OOAParameter"][row["ParameterID"].replace(".", "")].pk,
                 # TODO: not all code_ids appear in codes.csv e.g. verb-rel.pr_Attr-01
                 code_id=code_id,
                 value=row["Value"],
                 remark=row["Remark"],
                 # TODO: Source is not added as a proper foreign key. the csv contains several sources for one entry. This causes problems in sql
                 # TODO: It's a many to many relationship (a source may have several values and a value may have several sources). This usally requires a separate table.
                 # TODO: Check if clld offers some predefined table for that
                 source=";".join(row["Source"]),
                 coder=";".join(row["Coder"]),
                 )
        DBSession.flush()



def prime_cache(args):
    """If data needs to be denormalized for lookup, do that here.
    This procedure should be separate from the db initialization, because
    it will have to be run periodically whenever data has been updated.
    """
