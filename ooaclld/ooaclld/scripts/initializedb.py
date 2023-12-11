import collections
from pathlib import Path
import re
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
    # pattern to catch bib reference and optional page
    srcdescr = re.compile(r'^(.*?)\[(.*?)]$')
    # assert args.glottolog, 'The --glottolog option is required!'
    # args.log.info('Loading dataset')
    ds = args.cldf
    #ds = list(pycldf.iter_datasets(cldf_dir))[0]
    data = Data()
    data.add(
        common.Dataset,
        ooaclld.__name__,
        id=ooaclld.__name__,
        domain="ooaclld",
        publisher_name="TODO_ PUBLISHER",
        publisher_place="TODO_ PUBLISHER_ PLace",
        publisher_url="http://www.shh.mpg.de",
        license="http://creativecommons.org/licenses/by/4.0/",
        jsondata={
            "license_icon": "cc-by.png",  # TODO: replace with custome one
            "license_name": "Creative Commons Attribution 4.0 International License",
        },
        description="TODO: DESCRIPTION AS IN APICS: THE ATLAS OF PIDGIN..."
    )
    DBSession.flush()
    lrefs = collections.defaultdict(set)
    all_sources = set()
    for rec in tqdm(Database.from_file(ds.bibpath), desc="Processing sources"):
        ns = bibtex2source(rec, common.Source)
        if ns.id not in all_sources:
            all_sources.add(ns.id)
            data.add(common.Source, ns.id, _obj=ns)
    DBSession.flush()

    for row in tqdm(ds.iter_rows("contributors.csv"), desc="Processing contributors"):
        data.add(
            common.Contributor,
            row["ContributorID"],
            id=row["ContributorID"],
            name=row["Name"],
        )
    DBSession.flush()

    for c, row in enumerate(
        tqdm(ds.iter_rows("featuresets.csv"), desc="Processing featuresets")
    ):
        # reading the static page content into variable desc
        desc = None
        descr_path = ds.directory / "docs" / (row["Name"].lower() + ".md")
        if descr_path.exists():
            desc = open(descr_path, encoding="utf8").read()
        fset = data.add(
            models.OOAFeatureSet,
            row["FeatureSetID"],
            id=row["FeatureSetID"],
            name=row["Name"],
            domains=row["Domain"],
            authors=";".join(row["Authors"]),
            contributors=";".join(row["Contributors"] or [""]),
            filename=row["Filename"] or "",
            description=desc,
        )
        cnt = 0
        # TOdo: fix this issue in the data, then remove this part of the code
        # the problem is that an author cannot be as well a contributor
        authors = set(row["Authors"])
        contrib = set(row["Contributors"])
        row["Contributors"] = list(contrib - authors)
        for i, f in enumerate(["Authors", "Contributors"]):
            if row[f]:
                for co in row[f]:
                    data.add(
                        common.ContributionContributor,
                        co,
                        contribution=fset,
                        contributor_pk=data["Contributor"][co].pk,
                        primary=(i == 0),
                        ord=cnt,
                    )
                    cnt += 1
        DBSession.flush()

    for row in tqdm(ds.iter_rows("ParameterTable"), desc="Processing parameters"):
        data.add(
            models.OOAParameter,
            row["ParameterID"],
            id=row["ParameterID"],
            name=row["ParameterID"],
            featureset_pk=data["OOAFeatureSet"][row["FeatureSet"]].pk,
            featureset_name=row["FeatureSet"],  # TODO: delete that row
            question=row["Question"],
            datatype=row["datatype"],
            #visualization=row["VisualizationOnly"],
        )
    DBSession.flush()

    all_languages = {row["LanguageID"] for row in ds.iter_rows("ValueTable")}

    for row in tqdm(ds.iter_rows("LanguageTable"), desc="Processing languages"):
        if row["Glottocode"] not in all_languages:
            continue
        data.add(
            models.OOALanguage,
            row["Glottocode"],
            id=row["Glottocode"],
            glottocode=row["Glottocode"],
            name=row["Name"],
            latitude=row["Latitude"],
            longitude=row["Longitude"],
            macroarea=row["Macroarea"],
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

    for row in tqdm(ds.iter_rows("codes.csv"), desc="Processing codes"):
        data.add(
            common.DomainElement,
            row["CodeID"],#.replace(".", "").replace("]", ""),
            id=row["CodeID"],#.replace(".", "").replace("]", ""),
            description=row["Description"],
            jsondata={"icon": row["icons"]},
            parameter_pk=data["OOAParameter"][row["ParameterID"]].pk,
        )
    DBSession.flush()

    for c, row in enumerate(tqdm(ds.iter_rows("ValueTable"), desc="Processing values")):
        current_contribution = row["ID"].replace(".", "-").split("-")[0].split("_")[1]
        current_language = row["LanguageID"]
        current_param = row["ParameterID"]
        current_valueset_id = row["ID"]
        lpk = data["OOALanguage"][row["LanguageID"]].pk
        # add first valueset
        if c == 0:
            vs = data.add(
                common.ValueSet,
                row["ID"],
                id=row["ID"],
                language_pk=lpk,
                parameter_pk=data["OOAParameter"][row["ParameterID"].replace(".", "-")].pk,
                contribution_pk=data["OOAFeatureSet"][current_contribution].pk,
                # TODO: check that all values in the same valueset have the same source. If not, discuss with david
                #source=" & ".join(row['Source']),
            )

            if row['Source']:
                for s in row['Source']:
                    sid, desc = pycldf.Sources.parse(s)
                    if sid not in all_sources:
                        continue
                    # try:
                    #     s_, descr = srcdescr.search(s).groups()
                    # except AttributeError:
                    #     s_ = s
                    #     descr = ''
                    spk = data['Source'][sid].pk
                    data.add(common.ValueSetReference, s,
                             valueset=vs,
                             description=desc,
                             source_pk=spk)
                    if spk not in lrefs[lpk]:
                        lrefs[lpk].add(spk)
                    DBSession.flush()

            previous_con = current_contribution
            previous_lan = current_language
            previous_param = current_param
            previous_valueset_id = current_valueset_id

        if current_param != previous_param or current_language != previous_lan or current_contribution != previous_con:
            lpk = data["OOALanguage"][row["LanguageID"]].pk
            vs = data.add(
                common.ValueSet,
                row["ID"],
                id=row["ID"],
                language_pk=lpk,
                parameter_pk=data["OOAParameter"][row["ParameterID"].replace(".", "-")].pk,
                contribution_pk=data["OOAFeatureSet"][current_contribution].pk,
                # TODO: check that all values in the same valueset have the same source. If not, discuss with david
                #source=" & ".join(row['Source']),
            )
            DBSession.flush()
            if row['Source']:
                for s in row['Source']:
                    sid, desc = pycldf.Sources.parse(s)
                    if sid not in all_sources:
                        continue
                    # try:
                    #     s_, descr = srcdescr.search(s).groups()
                    # except AttributeError:
                    #     s_ = s
                    #     descr = ''
                    spk = data['Source'][sid].pk
                    data.add(common.ValueSetReference, s,
                             valueset=vs,
                             description=desc,
                             source_pk=spk)
                    if spk not in lrefs[lpk]:
                        lrefs[lpk].add(spk)
                DBSession.flush()

            previous_con = current_contribution
            previous_lan = current_language
            previous_param = current_param
            previous_valueset_id = current_valueset_id

        data.add(
            models.OOAValue,
            row["ID"],
            id=row["ID"],
            valueset_pk=data["ValueSet"][previous_valueset_id].pk,
            # Todo: not all values have a code id
            domainelement_pk=data["DomainElement"][row["CodeID"].replace(".", "-")].pk,
            code_id=row["CodeID"],
            value=row["Value"],
            remark=row["Remark"],
            coder=";".join(row["Coder"]),
        )
        DBSession.flush()
    # add language sources
    for lpk, spks in lrefs.items():
        for spk in spks:
            data.add(common.LanguageSource, lpk,
                     language_pk=lpk,
                     source_pk=spk)
    DBSession.flush()


def prime_cache(args):
    """If data needs to be denormalized for lookup, do that here.
    This procedure should be separate from the db initialization, because
    it will have to be run periodically whenever data has been updated.
    """
