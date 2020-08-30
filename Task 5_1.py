while True:
    first_number = int(input("First number: "))
    second_number = int(input("Second number: "))
    math_sign = str(input("+ - / * (0 - the end):\n"))
    if math_sign != "0":
        print("Your answer: ")
        if math_sign == '+':
            print(str(first_number + second_number),"\n")
        elif math_sign == '-':
            print(str(first_number - second_number),"\n")
        elif math_sign == '*':
            print(str(first_number * second_number),"\n")
        elif math_sign == '/' and second_number > 0:
            print(str(first_number / second_number),"\n")
        else:
            print('!The second number is < 0\n')
        continue
    else:
        print('Goodbye!')
        break
