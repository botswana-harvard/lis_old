from lis.core.lab_grading.classes import GradeFlag


class LabGradeFlag(GradeFlag):

    def __init__(self, reference_list, result_item, **kwargs):
        test_code = result_item.test_code
        gender = result_item.result.order.aliquot.receive.patient.gender
        dob = result_item.result.order.aliquot.receive.patient.dob
        drawn_datetime = result_item.result.order.aliquot.receive.receive_datetime
        release_datetime = result_item.result_item_datetime
        subject_identifier = result_item.result.subject_identifier
        subject_type = result_item.get_subject_type()
        super(LabGradeFlag, self).__init__(subject_identifier, subject_type, reference_list, test_code, gender, dob, drawn_datetime, release_datetime, **kwargs)
