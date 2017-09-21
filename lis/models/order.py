from django.db import models
from edc_base.model_mixins import BaseUuidModel


class Order(BaseUuidModel):

    order_identifier = models.CharField(
        max_length=25,
        editable=False,
        unique=True)

    aliquot_identifier = models.CharField(
        max_length=25)
