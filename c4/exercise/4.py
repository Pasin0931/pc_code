input_d = input("Input: ").split()
row = int(input_d[0])
column = int(input_d[1])

matrix = []
for i in range(row):
    nums = input().split()
    matrix.append(nums)

max = int(matrix[0][0]) + int(matrix[0][1]) + int(matrix[1][0]) + int(matrix[1][1])

for i_row in range(row - 1):
    for i_col in range(column - 1):
        sum = int(matrix[i_row][i_col]) + int(matrix[i_row][i_col + 1]) + int(matrix[i_row + 1][i_col]) + int(matrix[i_row + 1][i_col + 1])
        # print(matrix[i_row][i_col], matrix[i_row][i_col + 1], matrix[i_row + 1][i_col], matrix[i_row + 1][i_col + 1] + f" SUM: {sum}")
        if sum > max:
            max = sum
            # print(f"Max : {max}")

print("Output:")
print(max)