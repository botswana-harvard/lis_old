from django.db import models
from edc_base.model_mixins.base_uuid_model import BaseUuidModel


class Protocol(BaseUuidModel):

    name = models.CharField(
        max_length=25,
        unique=True)

    title = models.CharField(
        max_length=250,
        null=True,
        blank=True)

    def __str__(self):
        return self.name
