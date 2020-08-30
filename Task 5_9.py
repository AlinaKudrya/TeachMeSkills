m = int(input('From: '))
n = int(input('To: '))

for i in range(m, n+1):
    divisors = ''
    for j in range(2,i):
        if i % j == 0:
            divisors += str(j) + ' '
    print(f'{i}: {divisors}')