import csv
rssi = []
phase = []
channel = []
epc = []
with open('D:\\Atom\\Dependency\\tens.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        channel.append(row['CHANNEL'])
        epc.append(row['EPC'])
        phase.append(row['PHASE'])
        rssi.append(row['RSSI'])
print(rssi)
