from django.db import models
from django.utils.translation import ugettext as _

from edc_base.encrypted_fields import EncryptedCharField

from edc_base.model.models import BaseUuidModel


class AccountHolder(BaseUuidModel):

    first_name = EncryptedCharField(
        verbose_name=_("First name")
    )

    last_name = EncryptedCharField(
        verbose_name=_("Last name")
    )

    initials = models.CharField(max_length=3)

    comment = models.TextField(
        max_length=100,
        blank=True,)

    def __unicode__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return "/lab_account/accountholder/%s/" % self.id

    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = ['last_name', 'first_name']
        app_label = 'lab_account'
        db_table = 'bhp_lab_registration_accountholder'
