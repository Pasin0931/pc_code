# Name: Pasin Makcharoen # Student ID: 6810545794

in_ = int(input("Enter an odd number for the size: "))

if in_ % 2 == 0 or in_ <= 0:
    print("Error: Please enter a positive odd number.")
else:
    char_ = input("Enter the character to use: ")

    if char_.strip() != "" and len(char_) == 1:
        top_bottom = in_ // 2

        for i in range(top_bottom):
            if i == 0:
                print(" " * top_bottom + char_)
            else:
                print((" " * (top_bottom - i) + char_) + ((" " * ((i * 2) - 1)) + char_))

        print(char_ * in_)

        count = 1

        for i in range(top_bottom, 0, -1):
            if i == 1:
                print(" " * top_bottom + char_)
            else:
                print(((" " * count) + char_) + ((" " * ((i * 2) - 3)) + char_))
                count += 1
    else:
        print("Invalid input")