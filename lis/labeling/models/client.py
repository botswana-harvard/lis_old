from django.db import models

from edc_base.model.models import BaseUuidModel

from .label_printer import LabelPrinter


class Client(BaseUuidModel):
    """A model that links client or user's machine to a printer by IP address."""
    ip = models.GenericIPAddressField(
        verbose_name='IP Address',
        null=True,
        blank=True,
        help_text='may be determined from hostname'
    )

    name = models.CharField(
        verbose_name='Hostname',
        max_length=50,
        null=True,
        blank=True,
        help_text=''
    )

    label_printer = models.ForeignKey(
        LabelPrinter,
        help_text='printer to be selected for this client',
    )

    def __unicode__(self):
        return "{} ({})".format(self.name, str(self.label_printer))

    class Meta:
        app_label = 'labeling'
        ordering = ['ip', 'label_printer', ]
