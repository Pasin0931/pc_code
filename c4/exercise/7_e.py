input_d = input("Input: ").split()
rows = int(input_d[0])
columns = int(input_d[1])

matrix = []
for i in range(rows):
    nums = list(map(int, input().split()))
    matrix.append(nums)

dp = [[0] * columns for i in range(rows)]
# print(dp)
max_side = 0

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 1:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            if dp[i][j] > max_side:
                max_side = dp[i][j]

# print(dp)
print("Output:")
print(max_side)
