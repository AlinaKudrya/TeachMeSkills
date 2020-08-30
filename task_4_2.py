numbers = [1,2,3,4,5,6,7,8]
even_numbers = 0

print('FOR')
for i in numbers:
    if i % 2 == 0:
        even_numbers += 1
print(f"Number of even numbers = {even_numbers}",'\n')

#############

print('WHILE')
even_numbers = 0
counter = 0
while counter < len(numbers):
    if numbers[counter] % 2 == 0:
        even_numbers += 1
    counter += 1
print(f"Number of even numbers = {even_numbers}")