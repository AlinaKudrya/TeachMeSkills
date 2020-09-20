from exceptions import *
from func import mathematical_operation


def enter(sign, text):
    if sign == '':
        sign = input(text)
    return sign


def exit_or_continue():
    while True:
        yes_or_not = input('Do you want to continue? y/n: ')
        if yes_or_not == 'y':
            return True
        elif yes_or_not == 'n':
            return False
        else:
            print('--Incorrect answer--')
            continue


def ui():
    number1, number2, mathematical_sign = '', '', ''
    while True:
        number1 = enter(number1, '\nEnter the first number: ')
        if check_number(number1):
            mathematical_sign = enter(mathematical_sign, 'Enter the sign: ')
            if check_mathematical_sign(mathematical_sign):
                number2 = enter(number2, 'Enter the second number: ')
                if check_number(number2):
                    print(f'{number1} {mathematical_sign} {number2} = '
                          f'{mathematical_operation(mathematical_sign, number1, number2)}\n')
                    number1, number2, mathematical_sign = '', '', ''
                    if exit_or_continue():
                        continue
                    else:
                        break
                else:
                    number2 = ''
                    print('--Incorrect input. Try again--')
                    continue
            else:
                mathematical_sign = ''
                print('--Incorrect input. Try again--')
                continue
        else:
            number1 = ''
            print('--Incorrect input. Try again--')
            continue
