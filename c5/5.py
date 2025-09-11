# m = int(input('Enter m: '))
# n = int(input('Enter n: '))

# i = m

# while i <= n:
#     print(i)
#     i += 1



# _sum = 0
# _list = []

# exit_loop = False

# while exit_loop == False:

#     x = int(input('Enter x: '))
#     if x == -999:
#         exit_loop = True
#     else:
#         _list.append(x)
#         _sum += x

# print(_sum)
# print(_list)



# x = int(input('Enter start for outer loop: '))
# y = int(input('Enter start for inner loop: '))
# z = int(input('Enter stop for outer loop: '))
# w = int(input('Enter stop for inner loop: '))
# a = int(input('Enter step for outer loop: '))
# b = int(input('Enter step for inner loop: '))

# count_out = x

# while (count_out < z if a > 0 else count_out > z):

#     count_in = y

#     while (count_in < w if b > 0 else count_in > w):

#         if a == 0 or b == 0:
#             break

#         print(f"{count_out},{count_in}")
#         count_in += b

#     if a == 0 or b == 0:
#         break
    
#     count_out += a


# count = 0
# nums = []
# while True:
#     x = int(input("Enter x: "))
#     if x == -99:
#         break
#     nums.append(x)
#     count += 1
# print(f"Sum of {count} x's = {sum(nums)}")



# cumulative_sum = 0
# total_count = 0

# while True:
#     count = 0
#     nums = []
#     while True:
#         x = int(input("Enter x: "))
#         if x == -99:
#             break
#         nums.append(x)
#         count += 1

#     cumulative_sum += sum(nums)
#     total_count += count
#     print(f"Sum of {count} x's = {sum(nums)}")
#     print(f"Cumulative sum of {total_count} x's = {cumulative_sum}")

#     choice = input("Continue or quit (q for quit): ")
#     if choice == "q":
#         print()
#         break
#     print()



# def read_count_and_sum_x():
#     nums = []
#     count = 0

#     while True:
#         x = int(input("Enter x: "))
#         if x == -99:
#             break
#         nums.append(x)
#         count += 1

#     return sum(nums), count

# round = 1
# cumulative_sum = 0
# total_count = 0

# while True:
#     print(f"Round {round}:")

#     sum_n, count_nums = read_count_and_sum_x()

#     total_count += count_nums
#     cumulative_sum += sum_n
#     print(f"Sum of {count_nums} x's = {sum_n}")
#     print(f"Cumulative sum of {total_count} x's = {cumulative_sum}")

#     choice = input("Continue or quit (q for quit): ")
#     if choice == "q":
#         print()
#         break

#     round += 1
#     print()



# def read_cumulative_count_and_sum_x(cum_sum, cum_count):
#     nums = []
#     count = 0
#     while True:
#         x = int(input("Enter x: "))
#         if x == -99:
#             break
#         nums.append(x)
#         count += 1
#     return sum(nums) + cum_sum, count + cum_count

# round = 1
# cumulative_sum = 0
# total_count = 0

# while True:
#     # print()

#     sum_n, count_nums = read_cumulative_count_and_sum_x(cumulative_sum, total_count)

#     total_count = count_nums
#     cumulative_sum = sum_n
#     print(f"Round {round}: Cumulative sum of {total_count} x's = {cumulative_sum}")

#     choice = input("Continue or quit (q for quit): ")
#     if choice == "q":
#         print()
#         break

#     round += 1



# def read_list_x():
#     nums = []
#     while True:
#         x = int(input("Enter x: "))
#         if x == -99:
#             break
#         nums.append(x)
#     return nums

# round_num = 1
# cumulative_sum = 0
# total_count = 0
# all_lists = []

# while True:
#     print(f"Round {round_num}:")
    
#     current_list = read_list_x()
#     all_lists.append(current_list)

#     round_sum = sum(current_list)
#     round_count = len(current_list)
#     cumulative_sum += round_sum
#     total_count += round_count

#     print(f"Current list of x's = {current_list}")
#     print(f"Current nested list of x's = {all_lists}")
#     print(f"Cumulative sum of {total_count} x's = {cumulative_sum}")

#     choice = input("Continue or quit (q for quit): ")
#     if choice.lower() == "q":
#         print()
#         break

#     round_num += 1
#     print()



def factorial(x):
    sum_each_fact = []

    for i in range(1, x + 1):
        res = 1
        for j in range(i, 0, -1):
            # print(j, end=" ")
            res = res * j
        print(f"{i}! = {res}")
        sum_each_fact.append(res)

    return sum_each_fact

k = int(input("Input k: "))
result = sum(factorial(k))
print(f"Summation of factorial 1!-{k}! = {result}")