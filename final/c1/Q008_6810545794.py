# Name: Pasin Makcharoen # Student ID: 6810545794

in_ = int(input("Enter table size: "))

if in_ < 1:
    print("Invalid input")
else:
    count = 1

    for line in range(in_):
        for row_ in range(1, in_ + 1):
            print(f"{count*row_:>4}", end="")
        count += 1
        print()