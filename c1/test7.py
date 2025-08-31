def check_leap_year():
    year = int(input("What is the year (AD)? "))
    if year <= 0:
        print(f"Invalid input: the year must be positive")
    else:
        if year < 1751:
            if year % 4 == 0:
                print(f"The year {year} (AD) is a leap year")
            else:
                print("FFFFFFFFFFFFFFFF")
                print(f"The year {year} (AD) is not a leap year")
        elif year >= 1751:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                print(f"The year {year} (AD) is a leap year")
            else:
                print(f"The year {year} (AD) is not a leap year")

check_leap_year()