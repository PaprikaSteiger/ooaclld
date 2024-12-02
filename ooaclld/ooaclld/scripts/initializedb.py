import re
import itertools
import collections

import pycldf
from tqdm import tqdm

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
    data = Data()
    data.add(
        common.Dataset,
        "ATLAs",
        name="ATLAs",
        id="atlas",
        domain="the-url-we-will-use",
        publisher_name="TODO_ PUBLISHER",
        publisher_place="TODO_ PUBLISHER_ PLace",
        publisher_url="http://www.shh.mpg.de",
        license="http://creativecommons.org/licenses/by/4.0/",
        jsondata={
            "license_icon": "cc-by.png",  # TODO: replace with custome one
            "license_name": "Creative Commons Attribution 4.0 International License",
        },
        description="Areal Typology of Languages of the Americas"
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
        descr_path = ds.directory / "docs" / (row["FeatureSetID"] + ".md")
        if descr_path.exists():
            desc = open(descr_path, encoding="utf8").read()
        fset = data.add(
            models.OOAFeatureSet,
            row["FeatureSetID"],
            id=row["FeatureSetID"],
            name=row["Name"],
            domains=row["Domain"],
            authors=";".join(data['Contributor'][cid].name for cid in row["Authors"]),
            contributors=";".join(data['Contributor'][cid].name for cid in row["Contributors"]),
            description=desc,
        )
        cnt = 0
        # In CLLD, an author cannot also be a contributor
        # However, we have kept this structure of double-listing in the underlying CLDF
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
            name=row["Name"],
            featureset_pk=data["OOAFeatureSet"][row["FeatureSet"]].pk,
            question=row["Question"],
            datatype=row["datatype"],
        )
    DBSession.flush()

    for row in tqdm(ds.iter_rows("LanguageTable"), desc="Processing languages"):
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
        )
    DBSession.flush()

    for pid, rows in tqdm(itertools.groupby(
        sorted(ds.iter_rows("codes.csv"), key=lambda r: r['ParameterID']),
        lambda r: r['ParameterID']
    ), desc="Processing codes"):
        for i, row in enumerate(rows, start=1):
            data.add(
                common.DomainElement,
                row["CodeID"],
                id=row["CodeID"],
                description=row["Description"],
                name=row['Description'],
                number=i,
                jsondata={"icon": row["icons"]},
                parameter_pk=data["OOAParameter"][pid].pk,
            )
    DBSession.flush()

    for (lid, pid), rows in tqdm(itertools.groupby(
        sorted(ds.iter_rows('ValueTable'), key=lambda r: (r['LanguageID'], r['ParameterID'])),
        lambda r: (r['LanguageID'], r['ParameterID'])
    )):
        current_contribution = pid.split("-")[0]
        lpk = data["OOALanguage"][lid].pk
        # add first valueset
        vs = common.ValueSet(
            id='{}-{}'.format(lid, pid),
            language_pk=lpk,
            parameter_pk=data["OOAParameter"][pid.replace(".", "-")].pk,
            contribution_pk=data["OOAFeatureSet"][current_contribution].pk,
        )
        vsrefs = set()
        for row in rows:
            if row['Source']:
                for s in row['Source']:
                    sid, desc = pycldf.Sources.parse(s)
                    if sid not in all_sources:
                        continue
                    spk = data['Source'][sid].pk
                    if spk not in vsrefs:
                        data.add(
                            common.ValueSetReference, s,
                            valueset=vs,
                            description=desc,
                            source_pk=spk)
                        vsrefs.add(spk)
                    if spk not in lrefs[lpk]:
                        lrefs[lpk].add(spk)
                DBSession.flush()

            data.add(
                models.OOAValue,
                row["ID"],
                id=row["ID"],
                valueset=vs,
                domainelement_pk=data["DomainElement"][row["CodeID"].replace(".", "-")].pk,
                code_id=row["CodeID"],
                value=row["Value"],
                remark=row["Remark"],
                coder=";".join(row["Coder"]),
            )

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
