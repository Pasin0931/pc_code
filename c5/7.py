# def update_saving_list(saving_list, saving_today):
#     saving_list.append(saving_today)

# day = 1
# goal = float(input("Enter your goal amount: "))
# daily_allowance = float(input("Enter your daily allowance: "))

# saving = []
# collected = 0
 
# while goal > sum(saving):
#     amount_spent = float(input("Enter your money spent today: "))

#     collected = daily_allowance - amount_spent

#     update_saving_list(saving, collected)

#     if goal <= sum(saving):
#         break

#     print(f"Day {day}: amount collected today is {collected:.2f}.")
#     print(f"Amount collected so far is {sum(saving):.2f}. You need {goal - sum(saving):.2f} more to collect.")

#     day += 1

# print(f"Saving summary: {saving}")
# print(f"You totally collected {sum(saving):.2f} in {day} days.")



# def fah_to_cel(start, stop, step):
#     print(f"{'Fahrenheit':>12}{'Celcius':>12}")
#     print(f"{'----------':>12}{'-------':>12}")

#     f = start
#     while f < stop:
#         c = (f - 32) / 1.8
#         print(f"{f:>12.2f}{c:>12.2f}")
#         f += step

#     print(f"{'----------':>12}{'-------':>12}")

# print(fah_to_cel(10.5, 12.75, 0.25))



# def fah_to_cel(start, stop, step):
#     print(f"{'Fahrenheit':>12}{'Celcius':>12}")
#     print(f"{'----------':>12}{'-------':>12}")

#     if step == 0:
#         print(f"{'----------':>12}{'-------':>12}")
#         return

#     f = start

#     if step > 0:
#         while f < stop:
#             c = (f - 32) / 1.8
#             print(f"{f:12.2f}{c:12.2f}")
#             f += step

#     elif step < 0:
#         while f > stop:
#             c = (f - 32) / 1.8
#             print(f"{f:12.2f}{c:12.2f}")
#             f += step

#     print(f"{'----------':>12}{'-------':>12}")



# def printSleepTime(start_time,duration):
#     for time in range(start_time, duration + 1):
#        print(f"{time} min")

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



H = int(input("Enter the depth of the well: "))
U = int(input("Enter the height the frog can jump up: "))
D = int(input("Enter the height the frog slips down: "))

if U <= D:
    if H == U == D:
        print("The frog can escape the well on day 1.")
    else:
        print("The frog cannot get out of the well.")

else:
    frog_depth = H
    day = 0

    while True:
        day += 1
        frog_depth = frog_depth - U

        if frog_depth <= 0:
            break

        print(f"On day {day} the frog leaps to the depth of {frog_depth} meters.")

        frog_depth = frog_depth + D
        
        print(f"At night he slips down to the depth of {frog_depth} meters.")

    print(f"The frog can escape the well on day {day}.")