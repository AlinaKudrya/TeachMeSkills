matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(3):
    for j in range(3):
        if matrix[i][j] == max(matrix[i]):
            replace = matrix[i][j]
            matrix[i][j] = matrix[i][i]
            matrix[i][i] = replace
print(matrix)