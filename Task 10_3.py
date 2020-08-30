import csv
import datetime

dates = [
    ['25.12.2000'],
    ['11.01.2010'],
    ['01.06.2012'],
    ['09.08.2020'],
    ['05.03.2000']
]

dates_file = open('dates.csv','w')
csv.writer(dates_file).writerows(dates)
dates_file.close()

dates_file = open('dates.csv')
dates = dates_file.readlines()
for i in range(len(dates)):
    dates[i] = dates[i].replace('\n','')

earliest_date = datetime.datetime.strptime(dates[0], '%d.%m.%Y')

for i in range(len(dates)):
    if datetime.datetime.strptime(dates[i],'%d.%m.%Y') < earliest_date:
        earliest_date = datetime.datetime.strptime(dates[i], '%d.%m.%Y')

print(f"The earliest date in this list is: {earliest_date.date()}")