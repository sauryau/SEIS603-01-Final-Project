import pandas
import datetime

x = pandas.read_csv('Schedule_Times.csv')
print(x)

now = datetime.datetime.now()
today = datetime.datetime.strftime(now, '%m/%d/%Y')
print(today)

def get_times():
    todays_times = []
    for index, row in x.iterrows():
        if row['Date'] == today:
            date = row['Date']
            starttime = row['Start_Time']
            endtime = row['End_Time']
            todays_times.append([date,starttime,endtime])
    todays_times
    return (todays_times)

timeinput = get_times()
print(timeinput)



#print(row['Date'], row['Start_Time'], row['End_Time'])