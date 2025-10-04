# Name: Pasin Makcharoen # Student ID: 6810545794

in_ = input("Enter base and height: ").split()

mapped = list(map(float, in_))

if mapped[0] >= 0 and mapped[1] >= 0:
    caled = 0.5 * mapped[0] * mapped[1]
    print(f"Area: {caled:.2f}")
else:
    print("Input incorrect")