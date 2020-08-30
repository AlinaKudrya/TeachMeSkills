import random

numbers = []
for i in range(19):
    numbers.append(random.randint(1,100))

print(numbers)
maximum = max(numbers)
print(maximum)

for i in range(19):
    if numbers[i] % 2 == 0:
        numbers[i] = maximum

print(numbers)