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

print(f"Index of row with the maximum sum: {index} = {max_row_summ}")

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

print(f"Index of column with the maximum sum: {index} = {max_column_summ}")

index = 0
summ = 0
min_row_summ = sum(matrix[0])

for i in range(m):
    for j in range(n):
        summ += matrix[i][j]
    if summ < min_row_summ:
        min_row_summ = summ
        index = i
    summ = 0

print(f"Index of row with the minimum sum: {index} = {min_row_summ}")

index = 0
summ = 0
min_column_summ = 0

for i in range(m):
    min_column_summ += matrix[i][0]

for i in range(m):
    for j in range(n):
        summ += matrix[j][i]
    if summ < min_column_summ:
        min_column_summ = summ
        index = i
    summ = 0

print(f"Index of column with the minimum sum: {index} = {min_column_summ}\n")

print("Zeroing all elements above the main diagonal")
for i in range(m):
    for j in range(n):
        if i == j:
            for f in range(j+1,n):
                matrix[i][f] = 0
    print(matrix[i])

print("\nZeroing all elements below the main diagonal")
for i in range(m):
    for j in range(n):
        if i == j:
            for f in range(j):
                matrix[i][f] = 0
    print(matrix[i])

matrix_a = []
matrix_b = []

for i in range(m):
    matrix_a.append([])
    matrix_b.append([])
    for j in range(n):
        matrix_a[i].append(random.randint(1, 10))
        matrix_b[i].append(random.randint(1, 10))

print('\n2 new matrices:')
print(matrix_a)
print(matrix_b)

matrix_ab_sum = []

print(f'\nThe matrix equal to the sum of matrix_a and matrix_b:')

for i in range(m):
    matrix_ab_sum.append([])
    for j in range(n):
        matrix_ab_sum[i].append(matrix_a[i][j] + matrix_b[i][j])
    print(matrix_ab_sum[i])

matrix_ab_diff = []

print(f'\nThe matrix equal to the difference between matrix_a and matrix_b:')

for i in range(m):
    matrix_ab_diff.append([])
    for j in range(n):
        matrix_ab_diff[i].append(matrix_a[i][j] - matrix_b[i][j])
    print(matrix_ab_diff[i])

