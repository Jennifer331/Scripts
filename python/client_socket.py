import json
import socket
from util import epc_dtoh

HOST = 'localhost'
PORT = 8002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = s.recv(65536)
        try:
            for line in message.splitlines():
                tags = json.loads(line)
                for tag in tags:
                    print(epc_dtoh(tag['epc']), tag['channelInMhz'])
        except Exception as err:
            print(message)
            raise err




