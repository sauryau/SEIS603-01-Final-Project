import datetime
import sms_test_send

line= str('-----------------------')
print(datetime.datetime.now())
print('---------------------------')

put_on_patch = False
take_off_patch =False
put_on_time = datetime.datetime(2018,11,13,20,25)
take_off_time = put_on_time + datetime.timedelta(seconds=60)
while put_on_patch == False or take_off_patch == False:
    if datetime.datetime.now() >= put_on_time and put_on_patch==False:
        print('Put on the eye patch')
        print(datetime.datetime.now())
        print('----------------------------')
        sms_test_send.sendtext('Put on the patch')
        put_on_patch = True
    if datetime.datetime.now() >= take_off_time and take_off_patch==False:
        print('Take off the eye patch')
        print(datetime.datetime.now())
        sms_test_send.sendtext('Take off the eye patch')
        print('-----------------------------')
        take_off_patch = True

