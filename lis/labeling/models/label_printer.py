from django.db import models

from edc_base.model.models import BaseUuidModel


class LabelPrinter(BaseUuidModel):
    """A model of the printer name and IP address."""
    cups_printer_name = models.CharField(max_length=50)

    cups_server_hostname = models.CharField(
        max_length=25,
        help_text='must be a valid hostname in hosts file or DNS.'
        )

    cups_server_ip = models.GenericIPAddressField(
        null=True,
        help_text='provide if known.'
        )

    default = models.BooleanField(default=False)

    objects = models.Manager()

    def __unicode__(self):
        return '{}@{}'.format(self.cups_printer_name, self.cups_server_hostname,)

    class Meta:
        app_label = 'labeling'
        ordering = ['cups_printer_name', 'cups_server_hostname']
        unique_together = ['cups_printer_name', 'cups_server_hostname']
