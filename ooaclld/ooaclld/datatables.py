from sqlalchemy.orm import joinedload, contains_eager, subqueryload

from clld.web import datatables
from clld.web.datatables.base import Col, LinkCol, DetailsRowLinkCol, IdCol, DataTable
from clld.web.datatables.value import ValueNameCol
from clld.db.meta import DBSession
from clld.db.models import common
from clld.db.util import get_distinct_values, icontains
from clld.web.util.helpers import linked_contributors, link, contactmail
from clld.web.util.htmllib import HTML

from ooaclld.models import OOALanguage, OOAParameter, OOAUnit, OOAFeatureSet


class Features(datatables.Parameters):
    __constraints__ = [OOAFeatureSet]

    def base_query(self, query):
        if self.ooafeatureset:
            query = query.join(OOAFeatureSet)
            query = query.filter(OOAParameter.featureset_pk == self.ooafeatureset.pk)
        return query

    def col_defs(self):
        return [
            IdCol(self, 'ID', sClass='left'),
            Col(self, 'FeatureSet', model_col=OOAParameter.featureset_name, sClass='left'),
            Col(self, 'Questions', model_col=OOAParameter.question, sClass='left'),
            Col(self, 'Visualization', model_col=OOAParameter.visualization, sClass='left'),
            Col(self, 'Datatype', model_col=OOAParameter.datatype, sClass='left'),
        ]


class ContributorsCol(Col):
    def format(self, item):
        return linked_contributors(self.dt.req, item.contributor)


class Featuresets(datatables.Contributions):

    def col_defs(self):
        return [
            IdCol(self, 'Featureset ID', sClass='left'),
            Col(self, 'Domains', model_col=OOAFeatureSet.domains, sClass='left'),
            Col(self, 'Authors', model_col=OOAFeatureSet.authors, sClass='left'),
            Col(self, 'Contributors', model_col=OOAFeatureSet.contributors, sClass='left'),
            Col(self, 'Filename', model_col=OOAFeatureSet.filename, sClass='left'),
        ]


class Languages(datatables.Languages):
    def col_defs(self):
        return [
            IdCol(self, 'ID', sTitle='Glottocode', sClass='left'),
            Col(self, 'Macroarea', model_col=OOALanguage.macroarea, sClass='left'),
            Col(self, 'Family ID', model_col=OOALanguage.family_id, sClass='left')
        ]


class Units(datatables.Units):
    __constraints__ = [OOALanguage, OOAParameter]

    def base_query(self, query):
        if self.ooalanguage:
            query = query.join(OOALanguage)
            return query.filter(OOAUnit.language_pk == self.ooalanguage.pk)
        elif self.ooaparameter:
            query = query.join(OOAParameter)
            return query.filter(OOAUnit.parameter_pk == self.ooaparameter.pk)
        return query

    def col_defs(self):
        return [
            IdCol(self, 'Id', sTitle='id', sClass='left'),
            LinkCol(self, 'Parameter ID', model_col=OOAParameter.id, sClass='left', get_object=lambda i: i.parameter),
            LinkCol(self, 'Language ID', model_col=OOALanguage.id, sClass='left', get_object=lambda i: i.language),
            Col(self, 'Code ID', model_col=OOAUnit.code_id, sClass='left')
        ]


class Contributors(datatables.Contributors):

    def col_defs(self):
        return [
            IdCol(self, 'Contributor ID', model_col=common.Contributor.id, sClass='left'),
            Col(self, 'Name', model_col=common.Contributor.name, sClass='left')
        ]


def includeme(config):
    # the name of the datatable must be the same as the name given to the route pattern
    config.register_datatable('units', Units)
    config.register_datatable('languages', Languages)
    config.register_datatable('parameters', Features)
    config.register_datatable('featuresets', Featuresets)
    config.register_datatable('contributors', Contributors)

