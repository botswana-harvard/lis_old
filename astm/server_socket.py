import socket
from astm_classes.constants import ACK
from config.base_socket_config import TCP_IP, TCP_PORT, BUFFER_SIZE

MESSAGE = ["1H|\^&|||PSM^Roche Diagnostics^PSM^2.01.00.c|||||||P||20150109072546",
    "2P|1|WT38187|||^||||||||||||||||||20150109161000|||||||||",
    "3O|1|WT38187||ALL|R|20150109161000|||||X||||1||||||||||F",
    "4R|1|^^^CO2-L^^^^148.1|23.9179|||N||F||^System||20150109163033|148.1",
    "5L|1|N"]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
while 1:
    conn, addr = s.accept()
    for i in MESSAGE:
        data = conn.recv(BUFFER_SIZE)
        if data == ACK:
            conn.send(i)
conn.close()
