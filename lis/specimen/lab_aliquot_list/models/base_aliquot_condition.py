from edc_base.model.models import ListModelMixin

from ..managers import AliquotConditionManager


class BaseAliquotCondition(ListModelMixin):

    objects = AliquotConditionManager()

    def __str__(self):
        return "{0}: {1}".format(self.short_name.upper(), self.name)

    class Meta:
        abstract = True
