numbers = [1,2,3,4,5]
first_number = numbers[0]

print('FOR')
for i in range(len(numbers)-1):
    numbers[i] = numbers[i+1]
numbers[len(numbers)-1] = first_number
print(numbers, '\n')

#############

numbers = [1,2,3,4,5]
print('WHILE')
i = 0
while i != len(numbers)-1:
    numbers[i] = numbers[i+1]
    i += 1
numbers[len(numbers)-1] = first_number
print(numbers, '\n')