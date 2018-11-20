# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import datetime


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC523b8a138eea899153da4562c8d92f48'
auth_token = '88b5fbae4fd61a9c5a97936924eda4be'
client = Client(account_sid, auth_token)

# messages = client.messages.list()

def get_message_time(msg_nbr):
    messages = client.messages.list()
    last_message = (messages[msg_nbr])
    # print('From: ' + last_message.from_)
    # print('To: ' + last_message.to)
    # print('Message: ' + last_message.body)
    # print('Message API Date Sent: ' + str(last_message.date_sent))
    # print('Message API Date Created: ' + str(last_message.date_created))
    # print('Message API Date Updated: ' + str(last_message.date_updated))
    if last_message.body.find('Your time has been recorded as') != -1:
        recorded_time = last_message.body[-26:-7]
        # print(recorded_time)
        # print(type(recorded_time))
        # print('--------------------------------')
        recorded_time = datetime.datetime.strptime(recorded_time,'%Y-%m-%d %H:%M:%S')
        # print(recorded_time)
        # print(type(recorded_time))
    else:
        recorded_time = None
    return(recorded_time)
