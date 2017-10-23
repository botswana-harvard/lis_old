from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.utils import get_utcnow
from edc_base.model_validators.date import datetime_not_future

from .list_models import SpecimenType, SpecimenCondition


class ReceiveModelMixin(models.Model):

    receive_identifier = models.CharField(
        max_length=25,
        editable=False,
        unique=True)

    receive_datetime = models.DateTimeField(
        default=get_utcnow,
        validators=[datetime_not_future])

    collection_datetime = models.DateTimeField(
        validators=[datetime_not_future],
        help_text='Date and time specimen collected by customer')

    specimen_identifier = models.CharField(
        max_length=25,
        unique=True,
        help_text='The original unique specimen identifier from customer.')

    specimen_type = models.ForeignKey(SpecimenType, on_delete=PROTECT)

    specimen_condition = models.ForeignKey(
        SpecimenCondition, on_delete=PROTECT)

    specimen_volume = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=5.0,
        help_text='ml')

    protocol_number = models.CharField(
        max_length=25,
        help_text='Protocol or Account')

    site_code = models.CharField(
        max_length=25,
        null=True,
        blank=True)

    clinician_initials = models.CharField(
        verbose_name='Clinician\'s initials',
        max_length=3,
        null=True,
        blank=True)

    other_reference = models.CharField(
        max_length=25,
        null=True,
        blank=True)

    class Meta:
        abstract = True
