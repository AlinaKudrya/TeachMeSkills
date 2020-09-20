import re


def check_number(number):
    negative_number = re.match('[-]\d+', number)
    positive_number = re.match('\d+', number)
    if positive_number is not None and positive_number.group() == number:
        return True
    elif negative_number is not None and negative_number.group() == number:
        return True
    else:
        return False


def check_mathematical_sign(inputed_mathematical_sign):
    mathematical_sign = re.match('[+-/*]', inputed_mathematical_sign)
    if mathematical_sign is not None and mathematical_sign.group() == inputed_mathematical_sign:
        return True
    else:
        return False
