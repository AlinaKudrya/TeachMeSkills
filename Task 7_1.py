def convertation(action_number):
    answer = actions.get(action_number) * number
    return answer

actions = {
    1: 2.54,
    2: 0.39,
    3: 1.61,
    4: 0.62,
    5: 0.45,
    6: 2.21,
    7: 28.4,
    8: 0.04,
    9: 4.6,
    10: 0.22,
    11: 0.57,
    12: 0.76
}

while True:
    action = int(input('''1. Дюймы в сантиметры
2. Сантиметры в дюймы
3. Мили в километры
4. Километры в мили
5. Фунты в килограммы
6. Килограммы в фунты
7. Унции в граммы
8. Граммы в унции
9. Галлон в литры
10. Литры в галлоны
11. Пинты в литры
12. Литры в пинты
0. Exit \n
Choose an action: '''))
    if action != 0:
        number = int(input('\nEnter value: '))
        print(f'Your answer: {convertation(action)} \n')
        continue
    else:
        print('\nGoodbye!')
        break