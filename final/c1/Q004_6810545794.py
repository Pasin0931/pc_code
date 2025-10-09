# Name: Pasin Makcharoen # Student ID: 6810545794

size_ = input("Enter size of triangle: ")
pattern_ = input("Enter pattern string: ")

try:
    size_ = int(size_)

    temp = []
    for i in pattern_:
        if i == " ":
            continue
        else:
            temp.append(i)

    pattern_ = "".join(temp)

    if size_ <= 0 or pattern_ == "":
        print("Invalid input")
    else:
        index = 0
        for i in range(1, size_ + 1):
            for j in range(i):
                try:
                    print(pattern_[index], end="")
                    index += 1
                except IndexError:
                    index = 0
                    print(pattern_[index], end="")
                    index += 1
            print()
except ValueError:
    print("Invalid input")