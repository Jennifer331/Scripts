import json

buffer = []
msg1 = b'[{"epc": 1234, "name:ss}]\r\n[{"epc":5678, "name": yy}]\r\n[{"epc":910'
msg2 = b'0, "name": zz}]\r\n'

buffer = buffer + msg1.splitlines()
for i in range(len(buffer) - 1):
    buffer.pop(0)
print(buffer[0])
buffer[0] = buffer[0] + msg2
print(buffer[0])
