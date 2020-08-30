import datetime
import pprint

trains = [{
    'Train number': 12,
    'Point of arrival': 'Minsk',
    'Time of arrival': '12:45',
    'Point of departure': 'Lublin',
    'Time of departure': '01:20'
},
    {
        'Train number': 25,
        'Point of arrival': 'Minsk',
        'Time of arrival': '15:00',
        'Point of departure': 'Warszawa',
        'Time of departure': '09:30'
    },
    {
        'Train number': 65,
        'Point of arrival': 'Minsk',
        'Time of arrival': '10:00',
        'Point of departure': 'Brest',
        'Time of departure': '07:00'
    }
]

for i in trains:
    time_of_dep = datetime.datetime.strptime(i.get('Time of departure'), '%H:%M').time()
    time_of_arr = datetime.datetime.strptime(i.get('Time of arrival'), '%H:%M').time()
    travel_time = f'{abs(time_of_arr.hour - time_of_dep.hour)}:{abs(time_of_arr.minute-time_of_dep.minute)}'
    if datetime.datetime.strptime(travel_time,'%H:%M').time() > datetime.datetime.strptime('07:20','%H:%M').time():
        pprint.pprint(i)
        print(f'\nTravel time: {travel_time}')