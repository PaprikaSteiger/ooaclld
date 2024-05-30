from sqlalchemy.orm import joinedload, contains_eager, subqueryload

from clld.web import datatables
from clld.web.datatables.base import Col, LinkCol, DetailsRowLinkCol, DataTable
from clld.web.datatables.base import RefsCol as BaseRefsCol
from clld.web.datatables.value import ValueNameCol
from clld.db.meta import DBSession
from clld.db.models import common
from clld.db.models import (
    Value,
    ValueSet,
    ValueSetReference,
)
from sqlalchemy.orm import aliased
from clld.db.util import get_distinct_values, icontains
from clld.web.util.helpers import linked_contributors, link, contactmail, external_link, map_marker_img
from clld.web.util.htmllib import HTML, literal

from ooaclld.models import OOALanguage, OOAParameter, OOAFeatureSet, OOAValue

# special columns
class CommentCol(Col):
    __kw__ = {'bSortable': False, 'bSearchable': False, 'sTitle': ''}

    def format(self, item):
        return contactmail(
            self.dt.req, item.valueset, title="suggest changes")


class AuthorsCol(Col):
    def format(self, item):
        req = self.dt.req
        contribution = self._get_object(item) if self._get_object else item
        chunks = []
        for i, c in enumerate(contribution.primary_contributors):
            if i > 0:
                chunks.append(", ")
            chunks.append(link(req, c))
        if len(chunks) > 2:
            chunks[-2] = " and "
        return HTML.span(*chunks)


class AtlasIdCol(LinkCol):
    __kw__ = {'sClass': 'right', 'input_size': 'mini'}
    
    def get_attrs(self, item):
        return {'label': self.get_obj(item).id}
    
    def search(self, qs):
        if self.model_col:
            return icontains(self.model_col, qs)


class ContributorsCol(Col):
    def format(self, item):
        req = self.dt.req
        contribution = self._get_object(item) if self._get_object else item
        chunks = []

        for i, c in enumerate(contribution.secondary_contributors):
            if i == 0 and contribution.primary_contributors:
                chunks.append(" with ")
            if i > 0:
                chunks.append(", ")
            chunks.append(link(req, c))
        if len(chunks) > 2:
            chunks[-2] = " and "
        return HTML.span(*chunks)


class RefsCol(BaseRefsCol):

    """Listing sources for the corresponding ValueSet."""

    def get_obj(self, item):
        return item.valueset


class FeaturesetCol(LinkCol):
    def search(self, qs):
        return icontains(OOAFeatureSet.name, qs)

    def order(self):
        return OOAParameter.featureset_pk


# personalized tables
class Features(datatables.Parameters):
    __constraints__ = [OOAFeatureSet]

    def base_query(self, query):
        query = query.join(OOAFeatureSet)
        if self.ooafeatureset:
            query = query.filter(OOAParameter.featureset_pk == self.ooafeatureset.pk)
        return query

    def col_defs(self):
        return [
            AtlasIdCol(self, "ID", sTitle="ID", model_col=OOAParameter.id, sClass="left"),
            LinkCol(self, "Name", model_col=OOAParameter.name, sClass="left"),
            Col(self, "Question", model_col=OOAParameter.question, sClass="left"),
            FeaturesetCol(
                self,
                "FeatureSet",
                sTitle="Feature Set",
                sClass="left",
                get_object=lambda i: i.featureset,
                choices=get_distinct_values(OOAFeatureSet.name),
            ),
        ]

class Featuresets(datatables.Contributions):
    def col_defs(self):
        #cols = datatables.Contributions.col_defs(self)
        return [
            AtlasIdCol(self, "FeatureSet ID", sTitle="ID", model_col=OOAFeatureSet.id, sClass="left"),
            LinkCol(self, "Name", sTitle="Name", model_col=OOAFeatureSet.name, sClass="left"),
            #Col(self, "Domains", model_col=OOAFeatureSet.domains, sClass="left"),
            # ] + cols[:-1] + cols[-1:]
            AuthorsCol(self, "Authors", model_col=OOAFeatureSet.authors),
            ContributorsCol(self, "Contributors"),
            # Col(self, 'Contributors', model_col=OOAFeatureSet.contributors, sClass='left'),
            # Col(self, 'Filename', model_col=OOAFeatureSet.filename, sClass='left'),
        ]


class Languages(datatables.Languages):
    def col_defs(self):
        return [
            AtlasIdCol(self, "ID", sTitle="Glottocode", sClass="left", model_col=OOALanguage.id),
            LinkCol(self, "Name", sClass="left", model_col=OOALanguage.name),
            Col(self, "Family", sTitle="Family", model_col=OOALanguage.family_name, sClass="left"),
            Col(self, "Macroarea", model_col=OOALanguage.macroarea, sClass="left"),
            #Col(self, 'Latitude', model_col=OOALanguage.latitude),
            #Col(self, 'Longitude', model_col=OOALanguage.longitude),
        ]


class AtlasValueNameCol(ValueNameCol):
    def get_attrs(self, item):
        label = str(item.value) or 'NO_LABEL'
        label = HTML.span(map_marker_img(self.dt.req, item), literal('&nbsp;'), label)
        return {'label': label, 'title': str(item.value)}


class Values(datatables.Values):
    #__constraints__ = [OOAParameter, OOALanguage]

    def base_query(self, query):
        query = datatables.Values.base_query(self, query)
        if self.parameter:
            query = query.options(joinedload(Value.valueset).joinedload(common.ValueSet.language))
        return query

    def col_defs(self):
        if self.parameter:
            return [
                LinkCol(
                    self,
                    "Language ID",
                    sTitle="Language",
                    model_col=OOALanguage.id,
                    sClass="left",
                    get_object=lambda i: i.valueset.language,
                ),
                AtlasValueNameCol(self, "Value", sClass="left", choices=[de.name for de in self.parameter.domain]),
                Col(self, "Remark", model_col=OOAValue.remark, sClass="left"),
                RefsCol(self, 'Source'),
                CommentCol(self, 'c'),
            ]
        if self.language:
            return [
                LinkCol(
                     self, 
                     "Parameter ID", 
                     sTitle="Feature ID", 
                     sClass="left", 
                     model_col=OOAValue.parameter, 
                     get_object = lambda i: i.valueset.parameter),
                #IdCol(self, "Id", sTitle="Value ID", sClass="left"),
                LinkCol(
                    self,
                    "Feature ID",
                    sTitle="Feature",
                    model_col=OOAParameter.id,
                    sClass="left",
                    get_object=lambda i: i.valueset.parameter,
                ),
                AtlasValueNameCol(
                    self, "Value", model_col=OOAValue.value, sClass="left", bSortable=False, bSearchable=False),
                Col(self, "Remark", model_col=OOAValue.remark, sClass="left"),
                RefsCol(self, 'Source'),
                CommentCol(self, 'c'),
            ]


class Contributors(datatables.Contributors):
    def col_defs(self):
        return [
            #IdCol(
            #    self, "Contributor ID", sTitle="Contributor ID", model_col=common.Contributor.id, sClass="left"
            #),
            LinkCol(self, "Name", model_col=common.Contributor.name, sClass="left"),
        ]


def includeme(config):
    # the name of the datatable must be the same as the name given to the route pattern
    config.register_datatable("values", Values)
    config.register_datatable("languages", Languages)
    config.register_datatable("parameters", Features)
    config.register_datatable("contributions", Featuresets)
    config.register_datatable("contributors", Contributors)
