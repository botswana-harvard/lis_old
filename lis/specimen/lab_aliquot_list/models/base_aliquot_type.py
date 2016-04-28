from django.db import models

from django.core.validators import RegexValidator

from edc_base.model.models import BaseModel


class BaseAliquotType(BaseModel):

    name = models.CharField(
        verbose_name='Description',
        max_length=50,
    )

    alpha_code = models.CharField(
        verbose_name='Alpha code',
        validators=[
            RegexValidator('^[A-Z]{2,15}$')
        ],
        max_length=15,
        unique=True,
    )
    numeric_code = models.CharField(
        verbose_name='Numeric code (2-digit)',
        max_length=2,
        validators=[
            RegexValidator('^[0-9]{2}$')
        ],
        unique=True,
    )

    def __unicode__(self):
        return "{0} {1}: {2}".format(self.alpha_code, self.numeric_code, self.name.lower())

    def natural_key(self):
        return (self.alpha_code, self.numeric_code)

    class Meta:
        abstract = True
