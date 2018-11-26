import pandas
import datetime

x = pandas.read_csv('Schedule_Times.csv')
x['Date2'] = pandas.to_datetime(x['Date'], format='%m/%d/%Y')
# x['Start_Time'] = x['Date'].map(str) + x['Start_Time']
# print(x)

now = datetime.datetime.now()
today = datetime.datetime.strptime(datetime.datetime.strftime(now, '%Y-%m-%d'),'%Y-%m-%d')

def get_times():
    todays_times = []
    for index, row in x.iterrows():
        if row['Date2'] == today:
            # date = row['Date']
            date = datetime.datetime.strptime(str(row['Date2']),'%Y-%m-%d %H:%M:%S').date()
            starttime = datetime.datetime.strptime((row['Date'] + ' ' + row['Start_Time']), '%m/%d/%Y %I:%M %p')
            # starttime = row['Date'] + ' ' + row['Start_Time']
            endtime = datetime.datetime.strptime((row['Date'] + ' ' + row['End_Time']), '%m/%d/%Y %I:%M %p')
            # endtime = row['End_Time']
            todays_times.append([date,starttime,endtime])
            todays_times.sort()
    return (todays_times)



