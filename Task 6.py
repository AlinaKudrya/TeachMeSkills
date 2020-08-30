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
print(f'the maximum element of the matrix: {maximum}')

minimum = matrix[0][0]

for i in range(m):
    for j in range(n):
        if matrix[i][j] < minimum:
            minimum = matrix[i][j]
print(f'the minimum element of the matrix: {minimum}')

summ = 0

for i in range(m):
    for j in range(n):
        summ += matrix[i][j]

print(f'Sum of elements: {summ}')