from edc_base.model_mixins import BaseUuidModel, ListModelMixin


class SpecimenType(ListModelMixin, BaseUuidModel):
    pass


class SpecimenCondition(ListModelMixin, BaseUuidModel):
    pass
