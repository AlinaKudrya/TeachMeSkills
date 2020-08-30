numbers = [2,5,3,67,12,4]
print('FOR')
for i in range(len(numbers)):
    numbers[i] *= -2
print(numbers,'\n')

#############

numbers = [2,5,3,67,12,4]
print('WHILE')
number_of_numbers = 0

while number_of_numbers < len(numbers):
    numbers[number_of_numbers] *= -2
    number_of_numbers += 1

print(numbers)