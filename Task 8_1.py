numbers = [6,12,13,7,8]
print(numbers)

def factorial(number):
    fact = 1
    if number % 2 == 0:
        for i in range(2,number+1,2):
            fact *= i
    else:
        for i in range(1,number+1,2):
            fact *= i
    return fact

for i in range(5):
    print(factorial(numbers[i]))