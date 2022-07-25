from zope.interface import implementer
from sqlalchemy import (
    Column,
    String,
    Unicode,
    Integer,
    Boolean,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_property

from clld import interfaces
from clld.db.meta import Base, CustomModelMixin, PolymorphicBaseMixin
from clld.db.models import common, HasDataMixin, HasFilesMixin, IdNameDescriptionMixin, DataMixin, FilesMixin

from ooaclld.interfaces import IFeatureSet

from clld_glottologfamily_plugin.models import HasFamilyMixin


#-----------------------------------------------------------------------------
# specialized common mapper classes
#-----------------------------------------------------------------------------

@implementer(interfaces.ILanguage)
class OOALanguage(CustomModelMixin, common.Language):
    pk = Column(Unicode, ForeignKey('language.pk'), primary_key=True)
    glottocode = Column(Unicode)
    macroarea = Column(Unicode)
    iso = Column(Unicode)
    family_id = Column(Unicode)
    language_id = Column(Unicode)
    family_name = Column(Unicode)
    balanced = Column(Unicode)
    isolates = Column(Unicode)
    american = Column(Unicode)
    world = Column(Unicode)
    north_america = Column(Unicode)
    noun = Column(Unicode)


class OOAFeatureSet_data(Base, DataMixin):

    """Associated data mapper."""


class OOAFeatureSet_files(Base, FilesMixin):

    """Associated files mapper."""


@implementer(IFeatureSet)
class OOAFeatureSet(
    Base,
    PolymorphicBaseMixin,
    IdNameDescriptionMixin,
    HasDataMixin,
    HasFilesMixin
):
    #pk = Column(Unicode, ForeignKey('unitdomainelement.pk'))
    featureset_id = Column(Unicode)
    domains = Column(Unicode)
    authors = Column(Unicode)
    contributors = Column(Unicode)
    filename = Column(Unicode)


@implementer(interfaces.IParameter)
class OOAParameter(CustomModelMixin, common.Parameter):

    pk = Column(Unicode, ForeignKey('parameter.pk'), primary_key=True)
    parameter_id = Column(Unicode)

    #unitdomainelement_pk = Column(Unicode, ForeignKey('unitdomainelement.pk'))
    #unitdomainelement = relationship(common.UnitDomainElement)

    featureset_pk = Column(Unicode, ForeignKey('ooafeatureset.pk'))
    featureset = relationship(OOAFeatureSet, backref='ooafeatureset')

    question = Column(Unicode)
    datatype = Column(Unicode)
    visualization = Column(Unicode)


@implementer(interfaces.IUnit)
class OOAUnit(CustomModelMixin, common.Unit):
    pk = Column(Unicode, ForeignKey('unit.pk'), primary_key=True)

    parameter_pk = Column(Unicode, ForeignKey('parameter.pk'))
    parameter = relationship(OOAParameter)

    code_id = Column(Unicode)
    value = Column(Unicode)
    remark = Column(Unicode)
    source = Column(Unicode, ForeignKey('source.pk'))
    coder = Column(Unicode)


