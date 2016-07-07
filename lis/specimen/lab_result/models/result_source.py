from django.db import models

from edc_base.model.models import ListModelMixin


class ResultSource(ListModelMixin):

    objects = models.Manager()

    class Meta:
        app_label = 'lab_result'
        db_table = 'bhp_lab_core_resultsource'
