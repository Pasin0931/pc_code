# seq = [1,3,2,6]
# seq2 = [x*3 for x in seq]

# print(seq)
# print(seq2)



# N = 20
# s = [i for i in range(20) if i % 2 != 0]
# print(s)



# def f(n):
#     return sum((2* i + 5)**2 for i in range(1, n+1))
# print(f(1))



# nums = [i for i in range(1, 100) if i % 5 == 0 or i % 7 == 0]
# print(nums)



# N = 23
# s = [i for i in range(N+1) if i % 2 != 0 and i % 5 != 0]
# print(s)



# table = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# col0 = [i[0] for i in table]



table = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
new_table = [i for i in table if i[-1] % 2 == 0]
print(new_table)
# >>> new_table
# [[4, 5, 6], [10, 11, 12]]