import csv
import datetime

weather = [
    ['15.08.2020', 'Minsk', 27, 10],
    ['16.08.2020', 'Minsk', 25, 15],
    ['17.08.2020', 'Minsk', 21, 13],
    ['17.08.2020', 'Brest', 22, 13],
    ['18.08.2020', 'Minsk', 23, 18],
    ['19.08.2020', 'Minsk', 22, 14],
    ['19.08.2020', 'Brest', 26, 14],
    ['20.08.2020', 'Minsk', 21, 14],
    ['21.08.2020', 'Gomel', 26, 23],
    ['21.08.2020', 'Minsk', 17, 21],
    ['22.08.2020', 'Minsk', 18, 21],
    ['23.08.2020', 'Minsk', 21, 13]
]

weather_file = open('weather.csv', 'w')
weather_file_writer = csv.writer(weather_file)
weather_file_writer.writerow(['Date', 'Place', 'Degrees', 'Wind speed (km/h)'])
weather_file_writer.writerows(weather)
weather_file.close()

average_degrees = 0
average_wind_speed = 0

weather_file = open('weather.csv')
weather = weather_file.readlines()
for i in range(len(weather)):
    weather[i] = weather[i].replace('\n','').split(',')

print(weather[0])
for i in range(len(weather)):
    if weather[i][1] == 'Minsk':
        difference = datetime.datetime.now()-datetime.datetime.strptime(weather[i][0],'%d.%m.%Y')
        if 0 <= difference.days <= 6:
            average_wind_speed += int(weather[i][3])
            average_degrees += int(weather[i][2])
            print(weather[i])

print(f"Average weather in Minsk for a week: {round(average_degrees/7)} C. Average wind speed: {round(average_wind_speed/7)} km/h")