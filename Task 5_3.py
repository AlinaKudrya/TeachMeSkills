divisors_of_one_number = []
divisors_sums = {}

for i in range(200, 301):
    for j in range(1,i):
        if i % j == 0:
            divisors_of_one_number.append(j)
    divisors_sums[i] = sum(divisors_of_one_number)
    divisors_of_one_number = []

for i in divisors_sums:
    if i == divisors_sums.get(divisors_sums.get(i)):
        print(f'{i} == {divisors_sums.get(i)}')