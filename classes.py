class Math:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    @staticmethod
    def addition(number1, number2):
        return int(number1) + int(number2)

    @staticmethod
    def substraction(number1, number2):
        return int(number1) - int(number2)

    @staticmethod
    def multiplication(number1, number2):
        return int(number1) * int(number2)

    @staticmethod
    def division(number1, number2):
        if int(number2) != 0:
            return int(number1) / int(number2)
        else:
            return '!ERROR! -> Division by 0 is not possible'

    def mathematical_operation(self, the_sign):
        if the_sign == '+':
            return self.addition(self.number1, self.number2)
        if the_sign == '-':
            return self.substraction(self.number1, self.number2)
        if the_sign == '*':
            return self.multiplication(self.number1, self.number2)
        if the_sign == '/':
            return self.division(self.number1, self.number2)