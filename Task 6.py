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

index = 0
max_row_summ = 0
summ = 0

for i in range(m):
    for j in range(n):
        summ += matrix[i][j]
    if summ > max_row_summ:
        max_row_summ = summ
        index = i
    summ = 0

print(f"Index of row with the maximum sum: {index}")

index = 0
summ = 0
max_column_summ = 0

for i in range(m):
    for j in range(n):
        summ += matrix[j][i]
    if summ > max_column_summ:
        max_column_summ = summ
        index = i
    summ = 0

print(f"Index of column with the maximum sum: {index}")