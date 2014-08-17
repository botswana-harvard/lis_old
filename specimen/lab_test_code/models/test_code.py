from django.db import models

from .base_test_code import BaseTestCode
from .test_code_group import TestCodeGroup


class TestCode(BaseTestCode):

    test_code_group = models.ForeignKey(TestCodeGroup)

    class Meta:
        ordering = ['name']
        app_label = 'lab_test_code'
        db_table = 'bhp_lab_test_code_testcode'
