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
            IdCol(self, 'id', sClass='left'),
            LinkCol(self, 'parameter_id', model_col=OOAParameter.parameter_id),
            LinkCol(self, 'FeatureSet', model_col=OOAParameter.featureset_pk),
            Col(self, 'Questions', model_col=OOAParameter.question),
            Col(self, 'Visualization', model_col=OOAParameter.visualization),
            Col(self, 'Datatype', model_col=OOAParameter.datatype),
        ]


class Featuresets(datatables.Unitparameters):

    def col_defs(self):
        return [
            IdCol(self, 'featureset_id', sClass='left'),
            Col(self, 'Domains', model_col=OOAFeatureSet.domains),
            Col(self, 'Authors', model_col=OOAFeatureSet.authors),
            Col(self, 'Contributors', model_col=OOAFeatureSet.contributors),
            Col(self, 'Filename', model_col=OOAFeatureSet.filename),
        ]


class Languages(datatables.Languages):
    def col_defs(self):
        return [
            IdCol(self, 'id', sTitle='glottocode', sClass='left'),
            Col(self, 'macroarea', model_col=OOALanguage.macroarea),
            Col(self, 'family_id', model_col=OOALanguage.family_id)
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
            IdCol(self, 'id', sTitle='id'),
            Col(self, 'parameter_id', model_col=OOAUnit.parameter_pk),
            Col(self, 'language_id', model_col=OOAUnit.language_pk)
        ]


class Contributors(datatables.Contributors):

    def col_defs(self):
        return [
            IdCol(self, 'Contributor ID', model_col=common.Contributor.id),
            Col(self, 'Name', model_col=common.Contributor.name)
        ]


def includeme(config):
    # the name of the datatable must be the same as the name given to the route pattern
    config.register_datatable('units', Units)
    config.register_datatable('languages', Languages)
    config.register_datatable('parameters', Features)
    config.register_datatable('featuresets', Featuresets)
    config.register_datatable('contributors', Contributors)

