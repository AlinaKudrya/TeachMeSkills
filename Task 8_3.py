import math

n = int(input('Number of elements in row: '))


def Sin1(x, e):
    sin = 0
    for i in range(n):
        element = math.pow(-1, i) * math.pow(x, 2 * i + 1) / math.factorial(2 * i + 1)
        if abs(element) > e:
            sin += element
        #   print(f'{x}^{2*i+1}/{math.factorial(2*i+1)} = {element}')
    return sin


e = [10, 3.6, 15.0, 25.8, 32.2, 20.0]

for i in e:
    sinus = Sin1(5, i)
    print(round(sinus, 4))
