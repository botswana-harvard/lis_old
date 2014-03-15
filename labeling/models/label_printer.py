from django.db import models

from lis.base.model.models import BaseLabUuidModel


class LabelPrinter(BaseLabUuidModel):
    """A model of the printer name and IP address."""
    cups_printer_name = models.CharField(max_length=50)

    cups_server_ip = models.IPAddressField()

    default = models.BooleanField(default=False)

    objects = models.Manager()

    def __unicode__(self):
        return '%s@%s' % (self.cups_printer_name, self.cups_server_ip,)

#     def save(self, *args, **kwargs):
#         if self.default:
#             # set others to False
#             self.__class__.objects.all().update(default=False)
#         super(LabelPrinter, self).save(*args, **kwargs)

    class Meta:
        app_label = 'labeling'
#         db_table = 'lab_barcode_labelprinter'
        ordering = ['cups_server_ip', ]
