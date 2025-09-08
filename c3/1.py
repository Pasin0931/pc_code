# grid = [[1, 2], [3, 4]]
# for row in grid:
#     for val in row:
#         print(val)



# grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(grid)):
#     print(grid[i][i])



# grid = [[1, 2], [3, 4], [5, 6]]
# transposed = []
# for i in range(len(grid) - 1):
#     row = []
#     for j in range(len(grid)):
#         row.append(grid[j][i])
#     transposed.append(row)
# print(transposed)



# grid = [[2, 8], [6, 1], [5, 3]]
# max_val = grid[0][0]
# for row in grid:
#     for num in row:
#         if num > max_val:
#             max_val = num
# print(max_val)



# grid = [[".", "O", "."], ["X", ".", "O"]]
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if  grid[i][j] == ".":
#             grid[i][j] = "-"
# print(grid)



# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end="")
#         else:
#             print("-", end="")
#     print()



# data = [[12, 57, 64], [23, 48, 91], [50, 51, 42]]
# count = 0
# for row in data:
#     for value in row:
#         if value > 50:
#             count += 1
# print(count)



# for i in range(4):
#     for j in range(4):
#         if (i + j) % 2 == 0:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()



# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(index, fruit)



# squares = []
# for i in range(5):
#     squares.append(i * i)
# print(squares)



# items = ["pen", "pencil", "eraser"]
# for i, item in enumerate(items, start=1):
#     print(i, item[0])



# names = ["Tom", "", "Anna", "", "Sue"]
# for name in names:
#     if name == "":         
#         continue
#     print(name)



# names = ["Tom", "Tim", "Anna", "Tam", "Sue"]
# for name in names:
#     if "T" not in name:
#         continue
#     print(name)



# nums = [1, 2, 3, 4, 5, 6]
# result = []
# for n in nums:
#     if n % 2 == 0:
#         result.append(n * n)
# print(result)