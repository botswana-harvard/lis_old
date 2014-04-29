import datetime

from django.db import models
from django.core.urlresolvers import reverse

from lis.base.model.models import BaseLabListUuidModel

from ..choices import ALIQUOT_STATUS, SPECIMEN_MEASURE_UNITS, SPECIMEN_MEDIUM


class BaseAliquot (BaseLabListUuidModel):

    primary_aliquot = models.ForeignKey('self',
        null=True,
        related_name='primary',
        editable=False)

    source_aliquot = models.ForeignKey('self',
        null=True,
        related_name='source',
        editable=False,
        help_text='Aliquot from which this aliquot was created, Leave blank if this is the primary tube')

    aliquot_identifier = models.CharField(
        verbose_name='Aliquot Identifier',
        max_length=25,
        unique=True,
        help_text="Aliquot identifier",
        editable=False)

    aliquot_datetime = models.DateTimeField(
        verbose_name="Date and time aliquot created",
        default=datetime.datetime.today())

    count = models.IntegerField(
        editable=False,
        null=True)

    medium = models.CharField(
        verbose_name='Medium',
        max_length=25,
        choices=SPECIMEN_MEDIUM,
        default='TUBE')

    original_measure = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default='5.00')

    current_measure = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default='5.00')

    measure_units = models.CharField(
        max_length=25,
        choices=SPECIMEN_MEASURE_UNITS,
        default='mL')

    status = models.CharField(
        max_length=25,
        choices=ALIQUOT_STATUS,
        default='available')

    comment = models.CharField(
        max_length=50,
        null=True,
        blank=True)

    subject_identifier = models.CharField(
        max_length=50,
        null=True,
        editable=False,
        help_text="non-user helper field to simplify search and filtering")

    is_packed = models.BooleanField(
        verbose_name='packed',
        default=False,
        )

    receive_identifier = models.CharField(
        max_length=25,
        null=True,
        editable=False,
        help_text="non-user helper field to simplify search and filter")

    def __unicode__(self):
        return '%s' % (self.aliquot_identifier)

    def save(self, *args, **kwargs):
        self.receive_identifier = self.receive.receive_identifier
        super(BaseAliquot, self).save(*args, **kwargs)

    def get_subject_identifier(self):
        return self.subject_identifier

    def get_visit(self):
        return self.get_visit_model().objects.get(subject_identifier=self.get_subject_identifier())

    def drawn(self):
        return self.receive.drawn_datetime

    def barcode_value(self):
        return self.aliquot_identifier

    def to_receive(self):
        url = reverse('admin:{app_label}_receive_changelist'.format(app_label=self._meta.app_label,))
        return '<a href="{url}?q={receive_identifier}">{receive_identifier}</a>'.format(url=url, app_label=self._meta.app_label, receive_identifier=self.receive.receive_identifier)
    to_receive.allow_tags = True

    class Meta:
        abstract = True
