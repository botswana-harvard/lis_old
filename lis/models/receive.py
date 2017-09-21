from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel

from ..receive_helper import ReceiveHelper
from .patient import Patient
from .receive_model_mixin import ReceiveModelMixin


class Receive(ReceiveModelMixin, BaseUuidModel):

    patient = models.ForeignKey(Patient)

    age_in_years = models.IntegerField()

    history = HistoricalRecords()

    def __str__(self):
        return '{}: {}'.format(
            self.receive_identifier, self.receive_datetime.strftime('%Y-%m-%d %H:%M'))

    def save(self, *args, **kwargs):
        r = ReceiveHelper(
            receive_identifier=self.receive_identifier,
            collection_datetime=self.collection_datetime,
            dob=self.patient.dob)
        self.receive_identifier = r.receive_identifier
        self.age_in_years = r.age.years
        super().save(*args, **kwargs)

    class Meta:
        unique_together = (('patient', 'specimen_identifier'), )
