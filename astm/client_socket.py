import socket
from config.base_socket_config import TCP_IP, TCP_PORT, BUFFER_SIZE
from astm_classes.constants import ENCODING, ACK, EOT, NAK
from astm_classes.exceptions import Rejected
from astm_classes import codec
from astm_classes.mapping import (
    ConstantField, ComponentField, DateTimeField,
    TextField, Component, NotUsedField)
from astm_classes import __version__
from datetime import datetime
from astm_classes.records import (
    HeaderRecord, PatientRecord, OrderRecord, ResultRecord, TerminatorRecord
)


# Sender container to handle fields for the sender component
Sender = Component.build(
    TextField(name='device_type', default='PSM'),
    TextField(name='name', default='python-astm'),
    TextField(name='device_type', default='PSM'),
    TextField(name='version', default=__version__)
)

# Test container to store the fields for test component in the test id field.
Test = Component.build(
    NotUsedField(name='_'),
    NotUsedField(name='__'),
    NotUsedField(name='___'),
    TextField(name='test_id'),
    NotUsedField(name='_____'),
    NotUsedField(name='______'),
    NotUsedField(name='_______'),
    TextField(name='instrument_id')
)

Operator = Component.build(
    NotUsedField(name='_'),
    TextField(name='operator')
)

PatientName = Component.build(
    NotUsedField(name='_'),
    NotUsedField(name='')
)


# Handler class for the Header frame
class Header(HeaderRecord):
    sender = ComponentField(Sender)
    processing_id = ConstantField(default='P')
    created_at = DateTimeField(name='timestamp', default=datetime.now)


# Handler class for the Patient frame
class Patient(PatientRecord):
    practice_id = TextField(name='practice_id')
    name = ComponentField(PatientName)


# Handler class for the Order frame
class Order(OrderRecord):
    sample_id = TextField(name='sample_id')
    test = TextField(name='test')
    priority = TextField(name='priority')
    created_at = DateTimeField(name='created_at', default=datetime.now)
    action_code = TextField(name='action_code')
    biomaterial = TextField(name='biomaterial')
    report_type = TextField(name='report_type')


# Handler class for the Result frame
class Result(ResultRecord):
    test = ComponentField(Test)
    value = TextField(name='value')
    abonormal_flag = TextField(name='abnormal_flag')
    status = TextField(name='status')
    operator = ComponentField(Operator)
    date_completed = DateTimeField(name='completed_at')
    TextField(name='instrument')


# Handler class for the Terminator frame
class Terminator(TerminatorRecord):
    type = ConstantField(name='type', default='L')

decode_record = lambda r: codec.decode_record(r.encode(), ENCODING)
encode_record = lambda r: codec.encode(r, ENCODING)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

s.send(ACK)  # Send an Acknowledgement to sender to signal successful
while 1:
    data = s.recv(BUFFER_SIZE)
    seq = int(data[0])
    if data[0] == 'H':
        header = Header(*decode_record(data))
        s.send(ACK)
    counter = seq
    data = data[1:]
    if seq == counter:
        try:
            if data[0] == 'P':
                patient_data = Patient(*decode_record(data))
                print patient_data.practice_id
            elif data[0] == 'O':
                order_data = Order(*decode_record(data))
                print order_data.sample_id
            elif data[0] == 'R':
                result_data = Result(*decode_record(data))
                print "Result:"+result_data.test.test_id +":" + result_data.value
            else:
                if data[0] == 'L':
                    s.send(EOT)
        except:
            s.send(NAK)  # Send Not Acknowledged message back to the sender on error
            raise Rejected('')
    else:
        raise ValueError('Malformed ASTM frame. Inconsistent ASTM sequence numbers %r'
                         '' % seq + data)

    # Reset the counter to 0 when it reaches 7
    if counter == 7:
        counter = 0
    else:
        counter += 1
    s.send(ACK)  # Signal the sender to send another frame
