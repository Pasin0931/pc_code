# def matrix(h, w):
#     matrix = []
#     for height_i in range(h):
#         i = input("").split()
#         matrix.append(i)
#     print("Output: ")
#     for i in range(len(matrix)):
#         for j in matrix[i]:
#             print(j, end=" ")
#         print()

# temp = input("Input: ").split()
# temp[0] = int(temp[0])
# temp[1] = int(temp[1])

# matrix(temp[0], temp[1])



# def matrix(h, w):
#     matrix = []
#     for height_i in range(h):
#         i = input("").split()
#         matrix.append(i)
    
#     count = 0
#     for i in range(len(matrix)):
#         for j in matrix[i]:
#             if int(j) % 2 == 0:
#                 count+=1
#     print(f"Output: \n{count}")

# temp = input("Input: ").split()
# temp[0] = int(temp[0])
# temp[1] = int(temp[1])

# matrix(temp[0], temp[1])



# input_d = int(input("Input: "))
# matrix = []
# for i in range(input_d):
#     row = input("").split()
#     matrix.append(row)

# count = 0
# sum = 0
# for i in matrix:
#     sum = sum + int(i[count])
#     count += 1

# print(f"Output: \n{sum}")



# input_d = input("Input: ").split()
# matrix = []
# for i in range(int(input_d[0])):
#     row = input("").split()
#     matrix.append(row)

# print("Output:")
# for mat in matrix:
#     max = int(mat[0])
#     for i in mat:
#         if int(i) > int(max):
#             max = i
#     print(max)



# input_d = input("Input: ").split()
# matrix = []
# for i in range(int(input_d[0])):
#     row = input("").split()
#     matrix.append(row)

# print("Output:")
# for count_in in range(int(input_d[1])):
#     sum = 0
#     for i in range(int(input_d[0])):
#         sum = int(matrix[i][count_in]) + sum
#     print(sum)



# input_d = int(input("Input: "))
# matrix = []
# for i in range(input_d):
#     row = input("").split()
#     matrix.append(row)

# print("Output:")
# border_sum = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i == 0 or i == len(matrix[i]) - 1 or j == 0 or j == len(matrix[i]) - 1:
#             # print(matrix[i][j])
#             border_sum += int(matrix[i][j])

#     # for j in range(len(matrix[i])):
#     #     print(matrix[i][j])
#     # print("--------------")
# print(border_sum)



# input_d = int(input("Input: "))
# matrix = []
# for i in range(input_d):
#     row = input("").split()
#     matrix.append(row)

# print("Output:")
# rotated = [[0] * input_d for i in range(input_d)]
# for i in range(input_d):
#     for j in range(input_d):
#         rotated[j][input_d - 1 - i] = matrix[i][j]

# for row in rotated:
#     print(" ".join(row))



# input_d = input("Input: ").split()  # ---------------------------------
# matrix = []
# for i in range(int(input_d[0])):
#     row = input("").split()
#     matrix.append(row)

# print("Output: ", end="")
# right = True
# for i in range(len(matrix)):
#     if right == True:
#         for j in range(0, len(matrix[i]), 1):
#             print(matrix[i][j], end = " ")
#             right = False
#     else:
#         for j in range(len(matrix[i]) - 1, -1, -1):
#             print(matrix[i][j], end = " ")
#             right = True # -------------------------------------------



# r, c = map(int, input("Input: ").split())
# matrix = []
# for i in range(r):
#     row = input("").split()
#     matrix.append(row)

# print("Output:")

# result = []
# top, bottom, left, right = 0, r - 1, 0, c - 1

# while top <= bottom and left <= right:
#     # Traverse from Left to Right
#     for j in range(left, right + 1):
#         result.append(matrix[top][j])
#     top += 1

#     # Traverse from Top to Bottom
#     for i in range(top, bottom + 1):
#         result.append(matrix[i][right])
#     right -= 1

#     # Traverse from Right to Left
#     if top <= bottom:
#         for j in range(right, left - 1, -1):
#             result.append(matrix[bottom][j])
#         bottom -= 1

#     # Traverse from Bottom to Top
#     if left <= right:
#         for i in range(bottom, top - 1, -1):
#             result.append(matrix[i][left])
#         left += 1

# print(" ".join(result))



