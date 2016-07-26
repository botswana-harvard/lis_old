from django.db import models

from edc_base.model.validators import datetime_not_future

from ..choices import ORDER_STATUS


class BaseOrder(models.Model):

    order_identifier = models.CharField(
        verbose_name='Order number',
        max_length=25,
        help_text='Allocated internally',
        db_index=True,
        unique=True,
        editable=False)
    order_datetime = models.DateTimeField(
        verbose_name='Order Date',
        validators=[datetime_not_future],
        db_index=True)
    status = models.CharField(
        verbose_name='Status',
        max_length=25,
        choices=ORDER_STATUS,
        null=True,
        blank=False)
    comment = models.CharField(
        verbose_name='Comment',
        max_length=150,
        null=True,
        blank=True)
    import_datetime = models.DateTimeField(null=True)

    def __str__(self):
        return '%s %s' % (self.order_identifier, self.panel)

    class Meta:
        abstract = True
