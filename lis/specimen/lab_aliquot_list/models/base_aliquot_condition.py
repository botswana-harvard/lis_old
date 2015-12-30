from edc_base.model.models import BaseListModel

from ..managers import AliquotConditionManager


class BaseAliquotCondition(BaseListModel):

    objects = AliquotConditionManager()

    def __unicode__(self):
        return "{0}: {1}".format(self.short_name.upper(), self.name)

    class Meta:
        abstract = True
