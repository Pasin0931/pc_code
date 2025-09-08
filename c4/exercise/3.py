def read_matrix():
    rows = int(input("Input #rows? "))
    columns = int(input("Input #columns? "))
    
    matrix = []
    for i in range(1, rows+1):
        temp = []
        for j in range(1, columns+1):
            num = int(input(f"Input element[{i}][{j}]: "))
            temp.append(str(num))
        matrix.append(temp)
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        print("    ", end="")
        print("    ".join(matrix[i]))

def print_row(matrix):
    row_num = int(input('Input row number: '))
    print("    ", end="")
    print("    ".join(matrix[row_num - 1]))

def print_column(matrix):
    col_num = int(input('Input column number: '))
    for i in range(len(matrix)):
        print("    ", end="")
        print(matrix[i][col_num - 1], end="")

matrix = read_matrix()
print("Matrix A is")
print_matrix(matrix)
option = input("Print row(r) or column(c)? ")
if option == "r":
    print_row(matrix)
elif option == "c":
    print_column(matrix)