from django.db import models

from lis.base.model.models import BaseLabListModel


class ResultSource(BaseLabListModel):

    objects = models.Manager()

    class Meta:
        app_label = 'lab_result'
        db_table = 'bhp_lab_core_resultsource'
