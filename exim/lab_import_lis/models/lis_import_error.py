from django.db import models
from lis.base.model.models import BaseLabUuidModel


class LisImportError(BaseLabUuidModel):

    model_name = models.CharField(max_length=25)

    identifier = models.CharField(max_length=25)

    subject_identifier = models.CharField(max_length=25, null=True)

    error_message = models.TextField(max_length=250)

    objects = models.Manager()

    class Meta:
        app_label = 'lab_import_lis'
        ordering = ['-created']
