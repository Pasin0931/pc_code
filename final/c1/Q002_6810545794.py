# Name: Pasin Makcharoen # Student ID: 6810545794

in_ = input("Enter three integers: ").split()

mapped = list(map(int, in_))

sum_ = sum(mapped)
max_ = max(mapped)
min_ = min(mapped)

print("Sum: ", end="")

if sum_ == 0:
    print("Zero")
else:
    if sum_ % 2 == 0:
        print("Even")
    else:
        print("Odd")

print(f"Max: {max_}")
print(f"Min: {min_}")