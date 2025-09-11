input_d = input("Input: ").split()
rows = int(input_d[0])
columns = int(input_d[1])

matrix = []
for i in range(rows):
    nums = list(map(int, input().split()))
    matrix.append(nums)

result = [[0 for _ in range(columns)] for _ in range(rows)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(rows):
    for j in range(columns):
        total = 0
        count = 0
        for dx, dy in directions:
            ni = i + dx
            nj = j + dy
            if 0 <= ni < rows and 0 <= nj < columns:
                total += matrix[ni][nj]
                count += 1
        result[i][j] = total // count

print("Output:")
for row in result:
    print(' '.join(map(str, row)))
