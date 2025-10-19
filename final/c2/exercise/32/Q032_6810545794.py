# Name: Pasin Makcharoen # Student ID: 6810545794

from math import sqrt

while True:
    try:
        in_ = float(input("Enter a non-negative number: "))

        if in_ < 0:
            print("Error: Cannot calculate the square root of a negative number.")
        else:
            val_ = sqrt(in_)
            print(f"The square root of {in_:.1f} is {val_}.")
            break

    except ValueError:
        print("Error: Invalid input. Please enter a number.")