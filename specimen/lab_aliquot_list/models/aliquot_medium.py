from django.db import models

from lis.base.model.models import BaseLabListModel


class AliquotMedium(BaseLabListModel):

    objects = models.Manager()

    def __unicode__(self):
        return "%s" % (self.name.upper())

    class Meta:
        ordering = ["name"]
        app_label = 'lab_aliquot_list'
        db_table = 'bhp_lab_core_aliquotmedium'
