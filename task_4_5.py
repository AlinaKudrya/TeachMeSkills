first_number, second_number = int(input('Enter the first number: ')), int(input('Enter the second number: '))
fibonacci = [first_number, second_number]

print('FOR')
for i in range(15):
    fibonacci.append(fibonacci[i]+fibonacci[i+1])
print(fibonacci, '\n')

#############

fibonacci = [first_number, second_number]
print('WHILE')
counter = 0
while counter != 15:
    fibonacci.append(fibonacci[counter]+fibonacci[counter+1])
    counter += 1
print(fibonacci)