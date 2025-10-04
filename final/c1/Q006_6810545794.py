# Name: Pasin Makcharoen # Student ID: 6810545794

row_ = int(input("Enter number of rows: "))
col_ = int(input("Enter number of columns: "))

matrix = []

r = 1
for i in range(row_):
    r_ = input(f"Enter row {r}: ").split()
    matrix.append(r_)
    r += 1

transposed = []
for i in range(col_):
    transposed.append([])

for i in range(len(transposed)):
    for j in matrix:
        transposed[i].append(j[i])
    
print("\nTransposed Matrix:")
for i in transposed:
    for j in i:
        print(j, end=" ")
    print()