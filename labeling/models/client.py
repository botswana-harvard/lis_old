from django.db import models
from lis.base.model.models import BaseLabUuidModel
from .label_printer import LabelPrinter


class Client(BaseLabUuidModel):
    """A model that links client or user's machine to a printer by IP address."""
    ip = models.IPAddressField()

    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        )

    label_printer = models.ForeignKey(LabelPrinter)

    def __unicode__(self):
        return "%s - %s" % (self.ip, self.name,)

    class Meta:
        app_label = 'labeling'
        db_table = 'lab_barcode_client'
        ordering = ['ip', 'label_printer', ]
