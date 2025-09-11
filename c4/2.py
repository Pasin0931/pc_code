def transpose_matrix(matrix):
    transposed = []

    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        transposed.append(new_row)

    return transposed

temp = [[5,6,7],[8,9,10]]
print(transpose_matrix(temp))