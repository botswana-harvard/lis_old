from django.db import models

from lis.specimen.lab_receive.models import Receive
from lis.specimen.lab_aliquot_list.models import AliquotCondition, AliquotType

from ..managers import AliquotManager

from .base_aliquot import BaseAliquot


class Aliquot (BaseAliquot):

    receive = models.ForeignKey(Receive)

    aliquot_type = models.ForeignKey(AliquotType, verbose_name="Aliquot Type")

    aliquot_condition = models.ForeignKey(AliquotCondition,
        verbose_name="Aliquot Condition",
        default=10,
        null=True)

    parent_identifier = models.ForeignKey('self',
        to_field='aliquot_identifier',
        blank=True,
        null=True)

    objects = AliquotManager()

    def save(self, *args, **kwargs):
        self.subject_identifier = self.receive.patient.subject_identifier
        super(Aliquot, self).save(*args, **kwargs)

    def get_search_url(self):
        return "/laboratory/aliquot/search/aliquot/byword/%s/" % self.id

    class Meta:
        app_label = 'lab_aliquot'
        db_table = 'bhp_lab_core_aliquot'
