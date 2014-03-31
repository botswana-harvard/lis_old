from lis.base.model.models import BaseLabListModel

from ..managers import AliquotConditionManager


class BaseAliquotCondition(BaseLabListModel):

    objects = AliquotConditionManager()

    def __unicode__(self):
        return "{0}: {1}".format(self.short_name.upper(), self.name)

    class Meta:
        abstract = True
