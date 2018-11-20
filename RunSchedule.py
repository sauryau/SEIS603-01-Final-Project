import datetime
import sms_test_send
import ImportTimes

time_list = ImportTimes.get_times()
print(datetime.datetime.today().date())

for record in time_list:
    print(record)
print('--------------------------')


for record in time_list:
    # if datetime.datetime.today().date() == record[0] and datetime.datetime.now() <= record[1]:
    if datetime.datetime.now() <= record[1]:
        print(record)
        put_on_patch = False
        take_off_patch = False
        put_on_time = record[1]
        take_off_time = record[2]
        while put_on_patch == False or take_off_patch == False:
            if datetime.datetime.now() >= put_on_time and put_on_patch == False:
                print('Put on the eye patch')
                print(datetime.datetime.now())
                print('----------------------------')
                sms_test_send.sendtext('Put on the patch')
                put_on_patch = True
            if datetime.datetime.now() >= take_off_time and take_off_patch == False:
                print('Take off the eye patch')
                print(datetime.datetime.now())
                sms_test_send.sendtext('Take off the eye patch')
                print('-----------------------------')
                take_off_patch = True