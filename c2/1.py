# t = int(input("t: "))
# in_i = input("Input: ").split()

# count = 0

# for i in range(0, len(in_i) - 1):
#     for j in range(i + 1, len(in_i)):
#         if int(in_i[i]) + int(in_i[j]) == t:
#             count+=1

# print(f"Output: {count}")




# temp = ['g', 'n', 'i', 'n', 'e', 'v', 'e', ' ', 'd', 'o', 'o', 'G']
# temp.reverse()
# print(temp)




# seq = [10,11,10,9,12,9,8,10]
# seq.sort(reverse=True)

# print(seq)




# seq = [2,3,5,7,11,13,17,19]
# for i in range(len(seq) - 1, -1, -1):
#     print(seq[i])




seq = [2,3,5,7,11,13,17,19]
for i in range(1, len(seq), 3):
    print(seq[i])