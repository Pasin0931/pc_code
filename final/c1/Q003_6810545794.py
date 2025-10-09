# Name: Pasin Makcharoen # Student ID: 6810545794

in_ = int(input("Enter a non-negative integer: "))

if in_ < 0:
    print("Invalid input")
else:
    temp = []
    for i in range(in_, 0, -1):
        fac = 1
        for j in range(i, 0, -1):
            fac = fac * j
        temp.append(fac)

    print(f"Factorial Sum is: {sum(temp)}")
        