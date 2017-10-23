from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow
from edc_base.model_validators import datetime_not_future


class Order(BaseUuidModel):

    order_identifier = models.CharField(
        max_length=25,
        editable=False,
        unique=True)

    order_datetime = models.DateTimeField(
        default=get_utcnow,
        validators=[datetime_not_future])

    panel_name = models.CharField(
        max_length=25)

    aliquot_identifier = models.CharField(
        max_length=25)
