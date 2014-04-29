from datetime import datetime

from edc.subject.registration.models import RegisteredSubject

from ..models import ZplTemplate

from .model_label import ModelLabel


class AliquotLabel(ModelLabel):

    def __init__(self):
        super(AliquotLabel, self).__init__()
        template_name = 'aliquot_label'
        if not ZplTemplate.objects.filter(name=template_name):
            template_string = ("""^XA
                ^FO300,15^A0N,20,20^FD${protocol} Site ${site} ${clinician_initials}   ${aliquot_type} ${aliquot_count}${primary}^FS
                ^FO300,34^BY1,3.0^BCN,50,N,N,N
                ^BY^FD${aliquot_identifier}^FS
                ^FO300,92^A0N,20,20^FD${aliquot_identifier}^FS
                ^FO300,112^A0N,20,20^FD${subject_identifier} (${initials})^FS
                ^FO300,132^A0N,20,20^FDDOB: ${dob} ${gender}^FS
                ^FO300,152^A0N,25,20^FD${drawn_datetime}^FS
                ^XZ""")
            self.zpl_template = ZplTemplate.objects.create(
                name=template_name,
                template=template_string)
        else:
            self.zpl_template = ZplTemplate.objects.get(name=template_name)

    def refresh_label_context(self):
        aliquot = self.model_instance
        subject_identifier = aliquot.get_subject_identifier()
        registered_subject = RegisteredSubject.objects.get(subject_identifier=subject_identifier)
        primary = ''
        if aliquot.aliquot_identifier[-2:] == '01':
            primary = "<"
        custom = {}
        custom.update({
            'aliquot_identifier': aliquot.aliquot_identifier,
            'aliquot_count': aliquot.aliquot_identifier[-2:],
            'primary': primary,
            'barcode_value': aliquot.barcode_value(),
            'protocol': aliquot.aliquot_identifier[0:3],
            'site': aliquot.aliquot_identifier[3:5],
            'clinician_initials': aliquot.receive.clinician_initials,
            })
#         if 'hiv_status_code' in dir(aliquot):
#             custom.update({'hiv_status_code': str(aliquot.hiv_status_code()), })
#         if 'art_status_code' in dir(aliquot):
#             custom.update({'art_status_code': str(aliquot.art_status_code()), })
        custom.update({
            'drawn_datetime': aliquot.receive.drawn_datetime,
            'subject_identifier': subject_identifier,
            'gender': registered_subject.gender,
            'dob': registered_subject.dob,
            'initials': registered_subject.initials,
            'aliquot_type': aliquot.aliquot_type.alpha_code.upper()})
        self.label_context.update(**custom)

    def print_label_for_aliquot(self, request, aliquot):
        """ Prints a label flags this aliquot as 'labeled' to be called as an action."""
        if aliquot.aliquot_identifier:
            self.print_label(request, aliquot, 1)
            #aliquot.is_labeled = True
            aliquot.modified = datetime.today()
            aliquot.save()
