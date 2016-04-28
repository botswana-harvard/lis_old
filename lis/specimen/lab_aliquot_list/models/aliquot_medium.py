from django.db import models

from edc_base.model.models import BaseListModel


class AliquotMedium(BaseListModel):

    objects = models.Manager()

    def __unicode__(self):
        return "%s" % (self.name.upper())

    class Meta:
        ordering = ["name"]
        app_label = 'lab_aliquot_list'
        db_table = 'bhp_lab_core_aliquotmedium'
