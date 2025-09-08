input_d = int(input("Input: "))
is_symmetric = False

count = 0

matrix = []
for i in range(input_d):
    nums = input("").split()
    matrix.append(nums)

if input_d == 1:
    is_symmetric = True
else:
    for row in range(input_d - 1):
        for column in range(1 + count, input_d):
            # print(matrix[row][column], matrix[column][row])
            # print(f"[{row}][{column}] : [{column}][{row}]")
            if matrix[row][column] != matrix[column][row]:
                is_symmetric = False
                break
            else:
                is_symmetric = True
                continue
        if is_symmetric == False:
            break
        count+=1

print("Output:")
if is_symmetric == True:
    print("Yes")
else:
    print("No")