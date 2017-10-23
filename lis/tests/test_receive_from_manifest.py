from django.contrib.auth.models import User
from django.test import TestCase, tag
from edc_lab.models import Manifest, Box, BoxItem, BoxType, Shipper, Consignee, ManifestItem, Aliquot
from edc_lab.reports import ManifestReport, ManifestReportError
from pprint import pprint


@tag('1')
class TestReceiveFromManifest(TestCase):

    def setUp(self):
        self.user = User.objects.create(first_name='Noam', last_name='Chomsky')
        consignee = Consignee.objects.create(name='consignee')
        shipper = Shipper.objects.create(name='shipper')
        prefix = 'ABCDEFG'
        for i in range(0, 3):
            Aliquot.objects.create(count=i, aliquot_identifier=f'{prefix}{i}')
        self.manifest = Manifest.objects.create(
            consignee=consignee,
            shipper=shipper,
            site_code='site_code',
            site_name='site_name')

    def test_(self):
        self.manifest.shipped = True
        self.manifest.save()
        box_type = BoxType.objects.create(
            name='box_type', across=8, down=8, total=64)
        box = Box.objects.create(box_type=box_type)
        for index, obj in enumerate(Aliquot.objects.all()):
            BoxItem.objects.create(
                box=box,
                identifier=obj.aliquot_identifier,
                position=index)
        ManifestItem.objects.create(
            manifest=self.manifest, identifier=box.box_identifier)
        pprint(obj.__dict__)
