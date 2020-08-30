import random

m = int(input())
n = int(input())
matrix = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(random.randint(1, 15))
    print(matrix[i])

