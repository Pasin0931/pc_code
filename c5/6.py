# def list_factors(n):
#     res = ""
#     for i in range(1, n + 1):
#         if n % i == 0:
#             res += f"{i}, "
#     return res

# def find_sum_and_num_factors(n):
#     res = []
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             res.append(i)
#             count += 1
#     return sum(res), count

# count_inputs = 0
# count_primes = 0

# while True:
#     user_in = int(input("Please input N : "))
    
#     if user_in < 0:
#         print(f"Program reads {count_inputs} numbers. {count_primes} of them are prime.")
#         print("Program ends.")
#         print()
#         break
    
#     count_inputs += 1

#     factor_res = list_factors(user_in)
#     print(f"Factors of {user_in} are {factor_res}")

#     sum_fact, count = find_sum_and_num_factors(user_in)
#     print(f"Number of factors is {count}")
#     print(f"Sum of {factor_res}is {sum_fact}")

#     is_prime = True
#     if user_in <= 1:
#         is_prime = False
#     elif user_in == 2:
#         is_prime = True
#     elif user_in % 2 == 0:
#         is_prime = False
#     else:
#         for i in range(3, int(user_in**0.5) + 1, 2):
#             if user_in % i == 0:
#                 is_prime = False
#                 break

#     if is_prime:
#         print(f"{user_in} is prime number")
#         count_primes += 1
#     else:
#         print(f"{user_in} is not prime number")
#     print()



# def count_digits(number):
#     return len(str(number))

# def get_last_digit(n):
#     string_n = str(n)
#     last_digit = int(string_n[-1])
#     return last_digit

# def get_distribution(number):
#     num_str = str(number)[::-1]
#     terms = []
#     for i in range(len(num_str)):
#         digit = num_str[i]
#         terms.append(f"{digit}x10^{i}")
#     return " + ".join(terms)

# while True:
#     usr_input = int(input("Input number (negative number to quit): "))
#     if usr_input < 0:
#         break
#     print(f"{usr_input} = {get_distribution(usr_input)}")



# def printSleepTime(start_time,duration):
#     for time in range(start_time, duration + 1):
#         print(f"{time} min")


# nap_time = int(input("Input nap time: "))
# snooze_time = int(input("Input snooze time: "))

# current_time = 1

# printSleepTime(current_time, nap_time)
# while True:
#     choice = input("Alarm rings. Dismiss or Snooze: ")
#     if choice == "Dismiss":
#         break
#     else:
#         current_time = nap_time
#         nap_time += snooze_time
#         printSleepTime(current_time + 1, nap_time)


cumulative_digits = 0
while True:
    user_input = input("Enter number (E for exit): ")

    if user_input == 'E':
        print("Bye")
        break

    number = int(user_input)
    abs_str = str(abs(number))

    digit_count = len(abs_str)
    cumulative_digits = digit_count + cumulative_digits

    print(f"There are {digit_count} digits in {number}")
    print(f"Summation of digits is {cumulative_digits}")
