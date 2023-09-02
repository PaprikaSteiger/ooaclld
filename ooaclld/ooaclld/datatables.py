from sqlalchemy.orm import joinedload, contains_eager, subqueryload

from clld.web import datatables
from clld.web.datatables.base import Col, LinkCol, DetailsRowLinkCol, IdCol, DataTable
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


# personalized tables
class Features(datatables.Parameters):
    __constraints__ = [OOAFeatureSet]

    def base_query(self, query):
        if self.ooafeatureset:
            query = query.join(OOAFeatureSet)
            query = query.filter(OOAParameter.featureset_pk == self.ooafeatureset.pk)
        return query

    def col_defs(self):
        return [
            IdCol(self, "ID", sClass="left"),
            LinkCol(
                self,
                "FeatureSet",
                sTitle="FeatureSet",
                model_col=OOAFeatureSet.id,
                sClass="left",
                get_object=lambda i: i.featureset,
            ),
            AuthorsCol(
                self,
                "Authors",
                model_col=OOAFeatureSet.authors,
                sClass="left",
                get_object=lambda  i: i.featureset
            ),
            ContributorsCol(
                self,
                "Contributors",
                model_col=OOAFeatureSet.contributors,
                sClass="left",
                get_object=lambda i: i.featureset
            ),
            Col(self, "Questions", model_col=OOAParameter.question, sClass="left"),
            # Col(
            #     self,
            #     "Visualization",
            #     model_col=OOAParameter.visualization,
            #     sClass="left",
            # ),
            #Col(self, "Datatype", model_col=OOAParameter.datatype, sClass="left"),
        ]

class Featuresets(datatables.Contributions):
    def col_defs(self):
        #cols = datatables.Contributions.col_defs(self)
        return [
            IdCol(self, "FeatureSet ID", sTitle="FeatureSet ID", sClass="left"),
            LinkCol(self, "Name", model_col=OOAFeatureSet.name, sClass="left"),
            #Col(self, "Domains", model_col=OOAFeatureSet.domains, sClass="left"),
            # ] + cols[:-1] + cols[-1:]
            # Col(self, 'Authors', model_col=OOAFeatureSet.authors, sClass='left'),
            AuthorsCol(self, "Authors", model_col=OOAFeatureSet.authors),
            ContributorsCol(self, "Contributors"),
            # Col(self, 'Contributors', model_col=OOAFeatureSet.contributors, sClass='left'),
            # Col(self, 'Filename', model_col=OOAFeatureSet.filename, sClass='left'),
        ]


class Languages(datatables.Languages):
    def col_defs(self):
        return [
            IdCol(self, "ID", sTitle="Glottocode", sClass="left"),
            LinkCol(self, "Name", sClass="left", model_col=OOALanguage.name),
            Col(self, "Family Name", sTitle="Family Name", model_col=OOALanguage.family_name, sClass="left"),
            Col(self, "Macroarea", model_col=OOALanguage.macroarea, sClass="left"),
            Col(self, 'Latitude', model_col=OOALanguage.latitude),
            Col(self, 'Longitude', model_col=OOALanguage.longitude),
        ]


class ApicsValueNameCol(ValueNameCol):
    def get_attrs(self, item):
        label = str(item.value) or 'NO_LABEL'
        label = HTML.span(map_marker_img(self.dt.req, item), literal('&nbsp;'), label)
        return {'label': label, 'title': str(item.value)}

class Values(datatables.Values):
    #__constraints__ = [OOAParameter, OOALanguage]

    def base_query(self, query):
        query = query.join(aliased(ValueSet, flat=True)).options(
            joinedload(Value.valueset)
            .joinedload(ValueSet.references)
            .joinedload(ValueSetReference.source)
        )

        if self.language:
            query = query.join(ValueSet)
            return query.filter(ValueSet.language_pk == self.language.pk)

        if self.parameter:
            query = query.join(ValueSet)
            return query.filter(ValueSet.parameter_pk == self.parameter.pk)

        # if self.contribution:
        #     query = query.join(ValueSet.parameter)
        #     return query.filter(ValueSet.contribution_pk == self.contribution.pk)

        return query

    def col_defs(self):
        if self.parameter:
            return [
                IdCol(self, "Id", sTitle="Value ID", sClass="left"),
                LinkCol(
                    self,
                    "Feature ID",
                    sTitle="Feature ID",
                    model_col=OOAParameter.id,
                    sClass="left",
                    get_object=lambda i: i.valueset.parameter,
                ),
                LinkCol(
                    self,
                    "Language ID",
                    sTitle="Language ID",
                    model_col=OOALanguage.id,
                    sClass="left",
                    get_object=lambda i: i.valueset.language,
                ),
                ApicsValueNameCol(self, "Value", model_col=OOAValue.value, sClass="left"),
                Col(self, "Remark", model_col=OOAValue.remark, sClass="left"),
                RefsCol(self, 'Source'),
                CommentCol(self, 'c'),
            ]
        if self.language:
            return [
                #IdCol(self, "Id", sTitle="Value ID", sClass="left"),
                LinkCol(
                    self,
                    "Feature ID",
                    sTitle="Feature ID",
                    model_col=OOAParameter.id,
                    sClass="left",
                    get_object=lambda i: i.valueset.parameter,
                ),
                LinkCol(
                    self,
                    "Feature",
                    sTitle="Feature",
                    model_col=OOAParameter.name,
                    sClass="left",
                    get_object=lambda i: i.valueset.parameter,
                ),
                ApicsValueNameCol(self, "Value", model_col=OOAValue.value, sClass="left"),
                Col(self, "Remark", model_col=OOAValue.remark, sClass="left"),
                RefsCol(self, 'Source'),
                CommentCol(self, 'c'),
            ]


class Contributors(datatables.Contributors):
    def col_defs(self):
        return [
            IdCol(
                self, "Contributor ID", model_col=common.Contributor.id, sClass="left"
            ),
            LinkCol(self, "Name", model_col=common.Contributor.name, sClass="left"),
        ]


def includeme(config):
    # the name of the datatable must be the same as the name given to the route pattern
    config.register_datatable("values", Values)
    config.register_datatable("languages", Languages)
    config.register_datatable("parameters", Features)
    config.register_datatable("contributions", Featuresets)
    config.register_datatable("contributors", Contributors)
