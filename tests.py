import datetime
import sms_test_send
import ImportTimes
import get_last_reponse
import time

time_list = ImportTimes.get_times()
print(datetime.datetime.today().date())

for record in time_list:
    print(record)
print('--------------------------')

sms_test_send.sendtext('Program has started')

time.sleep(10)

# if get_last_reponse.get_message_time(0) is not None:
#     print('----------------------')
#     print('last message time is not none')
#     print(get_last_reponse.get_message_time(0))
#     print(type(get_last_reponse.get_message_time(0)))
#     print('----------------------')

for record in time_list:
    # if datetime.datetime.today().date() == record[0] and datetime.datetime.now() <= record[1]:
    if datetime.datetime.now() <= record[1]:
        print(record)
        put_on_patch = False
        take_off_patch = False
        take_off_time_updated = False
        put_on_time = record[1]
        take_off_time = record[2]
        while put_on_patch == False or take_off_patch == False:
            # last_response_time = get_last_reponse.get_message_time(0)
            # print(last_response_time)
            if datetime.datetime.now() >= put_on_time and put_on_patch == False:
                print('Put on the eye patch: sent at - ' + str(datetime.datetime.now()))
                print(datetime.datetime.now())
                print('----------------------------')
                sms_test_send.sendtext('Put on the patch: sent at - ' + str(datetime.datetime.now()))
                put_on_patch = True
            if get_last_reponse.get_message_time(0) is not None and take_off_patch == False and put_on_patch == True and take_off_time_updated == False:
                print('---get last time is not none----')
                last_response_time = get_last_reponse.get_message_time(0)
                print('The put on response time was: ' + str(last_response_time))
                put_on_time_delay = last_response_time - put_on_time
                print('The put on time delay was: ' + str(put_on_time_delay))
                take_off_time = take_off_time + put_on_time_delay
                print('The new take off time is: ' + str(take_off_time))
                # take_off_time = last_response_time
                take_off_time_updated = True
                print('---get last time is not none----')
            if datetime.datetime.now() >= take_off_time and take_off_patch == False:
                print('Take off the eye patch')
                print(datetime.datetime.now())
                sms_test_send.sendtext('Take off the eye patch: sent at - ' + str(datetime.datetime.now()))
                print('-----------------------------')
                take_off_patch = True