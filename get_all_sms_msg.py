# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import csv
import pandas

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC523b8a138eea899153da4562c8d92f48'
auth_token = '88b5fbae4fd61a9c5a97936924eda4be'
client = Client(account_sid, auth_token)

messages = client.messages.list()

message_list = []
for record in messages:
    print('From: ' + record.from_ + ' To: ' + record.to)
    print(record.body)
    print(record.date_sent)
    print(type(record.body))
    sublist = [record.from_, record.to, record.date_sent, record.body]
    message_list.append(sublist)
    print('----------------------------------')

print(message_list)
print(type(message_list))
print(len(message_list))

with open('testfile.csv', "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for i in message_list:
            writer.writerow([i])

pandaslist = pandas.DataFrame(message_list)
print(pandaslist)
pandaslist.to_csv('pandacsv.txt')



