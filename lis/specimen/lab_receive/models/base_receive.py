from datetime import datetime

from django.db import models

from edc_base.model.validators import datetime_not_future
from edc_base.model.fields import InitialsField


class BaseReceive (models.Model):

    receive_identifier = models.CharField(
        verbose_name='Receiving Identifier',
        max_length=25,
        null=True,  # should not be True
        editable=False,
        db_index=True,
        unique=True)

    requisition_identifier = models.CharField(
        verbose_name='Requisition Identifier',
        max_length=25,
        null=True,
        blank=True,
        db_index=True)

    drawn_datetime = models.DateTimeField(
        verbose_name="Date and time drawn",
        validators=[datetime_not_future, ],
        db_index=True)

    receive_datetime = models.DateTimeField(
        verbose_name="Date and time received",
        default=datetime.now(),
        validators=[datetime_not_future, ],
        db_index=True)

    visit = models.CharField(
        verbose_name="Visit Code",
        max_length=25)

    clinician_initials = InitialsField()

    receive_condition = models.CharField(
        verbose_name='Condition of primary tube',
        max_length=50,
        null=True)

    import_datetime = models.DateTimeField(null=True)

    def __unicode__(self):
        return '{0}'.format(self.receive_identifier)

    class Meta:
        abstract = True
