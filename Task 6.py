import random
matrix = []
maximum = 0

m = int(input())
n = int(input())

for i in range(m):
    matrix.append([])
    for j in range(n):
        matrix[i].append(random.randint(1, 20))
    print(matrix[i])

for i in range(m):
    for j in range(n):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
print(maximum)

minimum = matrix[0][0]

for i in range(m):
    for j in range(n):
        if matrix[i][j] < minimum:
            minimum = matrix[i][j]
print(minimum)