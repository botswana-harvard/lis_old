from lis.core.lab_reference.models import BaseReferenceList


class TestCodeReferenceList(BaseReferenceList):

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'lab_test_code'
        db_table = 'bhp_lab_test_code_testcodereferencelist'
        ordering = ['name', ]
