def is_leap_year(year):
    if year <= 0:
        return False
    else:
        if year <= 1751:
            if year % 4 == 0:
                return True
            else:
                return False
        elif year > 1751:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                return True
            else:
                return False
            
def find_num_days_in_month(month, isLeap=False):
    if month == 1:
        day = 31

    elif month == 2:
        if isLeap == True:
            day = 29
        else:
            day = 28

    elif month == 3:
        day = 31

    elif month == 4:
        day = 30

    elif month == 5:
        day = 31

    elif month == 6:
        day = 30

    elif month == 7:
        day = 31

    elif month == 8:
        day = 31

    elif month == 9:
        day = 30

    elif month == 10:
        day = 31

    elif month == 11:
        day = 30

    elif month == 12:
        day = 31

    return day

def find_remaining_days_in_year(month, date, day_in_month, isLeap=False):
    total_days = day_in_month - date
    month+=1

    for i in range(month, 13):
        total_days += find_num_days_in_month(i, isLeap)

    return total_days + 1


day = int(input("Input day? "))
month = int(input("Input month? "))
year = int(input("Input year? "))

leap_year = is_leap_year(year)
num_days = find_num_days_in_month(month, leap_year) + 1
day_remaining_month = num_days - day
day_remaining_year = find_remaining_days_in_year(month, day, num_days, leap_year)

if leap_year == True:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
print(f"There are {day_remaining_month} days remaining in current month.")
print(f"There are {day_remaining_year - 1} days remaining in current year.")


print(is_leap_year(400))
print(is_leap_year(1800))
print(is_leap_year(2400))
print(find_num_days_in_month(3, True))
print(find_num_days_in_month(3))
print(find_num_days_in_month(4))
print(find_num_days_in_month(2, True))
print(find_num_days_in_month(2, False))
print(find_remaining_days_in_year(2, 21, 29, True))
print(find_remaining_days_in_year(2, 21, 28))
print(find_remaining_days_in_year(8, 6, 31))