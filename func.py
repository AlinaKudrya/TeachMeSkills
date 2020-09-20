def addition(number1, number2):
    return int(number1) + int(number2)


def substraction(number1, number2):
    return int(number1) - int(number2)


def multiplication(number1, number2):
    return int(number1) * int(number2)


def division(number1, number2):
    if int(number2) != 0:
        return int(number1) / int(number2)
    else:
        return '!ERROR! -> Division by 0 is not possible'


def mathematical_operation(the_sign, number1, number2):
    if the_sign == '+':
        return addition(number1, number2)
    if the_sign == '-':
        return substraction(number1, number2)
    if the_sign == '*':
        return multiplication(number1, number2)
    if the_sign == '/':
        return division(number1, number2)
