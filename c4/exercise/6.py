input_d = input("Input: ").split()
rows = int(input_d[0])
columns = int(input_d[1])

matrix = []
for i in range(rows):
    nums = list(map(int, input().split()))
    matrix.append(nums)

saddle_point_count = 0
current_row = 0
current_col = 0
for row in range(rows):
    min = int(matrix[row][0])
    current_col = 0
    current_row = row
    for col in range(columns):
        if int(matrix[row][col]) < min:
            min = int(matrix[row][col])
            current_row = row
            current_col = col
            # print(min)
    
    max = int(matrix[current_row][current_col])
    state_saddle = True

    for row_in in range(rows):
        if int(matrix[row_in][current_col]) > max:
            state_saddle = False
            break

    if state_saddle == True:
        saddle_point_count += 1
        
print("Output:")
print(saddle_point_count)