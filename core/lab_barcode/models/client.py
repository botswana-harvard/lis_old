from django.db import models
from lis.base.model.models import BaseLabUuidModel
from .label_printer import LabelPrinter


class Client(BaseLabUuidModel):

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
        app_label = 'lab_barcode'
        ordering = ['ip', 'label_printer', ]
