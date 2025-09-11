def matrix(n):
    matrix_table = []
    for row in range(n):
        column_matrix = []
        for column in range(0, n):
            input_val = int(input(f"Input element[{row + 1}][{column + 1}]: "))
            column_matrix.append(input_val)
        matrix_table.append(column_matrix)

    return matrix_table

def sum_diagonal(matrix):
    tl_br = []
    tr_bl = []
    tr = (-1 * len(matrix)) - 1

    for i in range(len(matrix)):
        tl_br.append(matrix[i][i])
    
    for i in range(-1, tr, - 1):
        tr_bl.append(matrix[i][(i*-1) - 1])

    # print(sum(tl_br))
    # print(sum(tr_bl))

    return (f"Sum of its diagonal elements (top-left to bottom-right) is {sum(tl_br)}\n"
            f"Sum of its diagonal elements (top-right to bottom-left) is {sum(tr_bl)}")

n = int(input("Input n: "))
this_matrix = matrix(n)
print(sum_diagonal(this_matrix))