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
from clld.db.models import common

from clld_glottologfamily_plugin.models import HasFamilyMixin


# -----------------------------------------------------------------------------
# specialized common mapper classes
# -----------------------------------------------------------------------------


@implementer(interfaces.ILanguage)
class OOALanguage(CustomModelMixin, common.Language):
    pk = Column(Integer, ForeignKey("language.pk"), primary_key=True)
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


@implementer(interfaces.IContribution)
class OOAFeatureSet(CustomModelMixin, common.Contribution):
    pk = Column(Integer, ForeignKey("contribution.pk"), primary_key=True)
    featureset_id = Column(Unicode)
    domains = Column(Unicode)
    authors = Column(Unicode)
    # contributor = relationship(common.Contributor)
    contributors = Column(Unicode)
    filename = Column(Unicode)


@implementer(interfaces.IParameter)
class OOAParameter(CustomModelMixin, common.Parameter):
    pk = Column(Integer, ForeignKey("parameter.pk"), primary_key=True)

    featureset_pk = Column(Integer, ForeignKey("contribution.pk"))
    featureset_name = Column(Unicode)
    featureset = relationship(common.Contribution)

    question = Column(Unicode)
    datatype = Column(Unicode)


@implementer(interfaces.IValue)
class OOAValue(CustomModelMixin, common.Value):
    pk = Column(Integer, ForeignKey("value.pk"), primary_key=True)
    remark = Column(Unicode)
    value = Column(Unicode)
    code_id = Column(Unicode)
    parameter = Column(Integer, ForeignKey("parameter.pk"))
    # TODO: Maybe add a relationship to contributors
    coder = Column(Unicode)

    def __str__(self):
        return self.id
