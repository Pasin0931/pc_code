input_d = input("Input: ").split()
rows = int(input_d[0])
columns = int(input_d[1])

matrix = []
for i in range(rows):
    nums = list(map(int, input().split()))
    matrix.append(nums)

# print(matrix)
state = True

for row in range(rows):
    for col in range(row + 1, columns):
        if matrix[row][col] != 0:
            state = False
            break

print("Output:")
if state == True:
    print(True)
else:
    print(False)