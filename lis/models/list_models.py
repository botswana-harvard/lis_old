from edc_base.model_mixins.list_model_mixin import ListModelMixin
from edc_base.model_mixins import BaseUuidModel


class SpecimenType(ListModelMixin, BaseUuidModel):
    pass


class SpecimenCondition(ListModelMixin, BaseUuidModel):
    pass
