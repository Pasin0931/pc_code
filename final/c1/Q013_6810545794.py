# Name: Pasin Makcharoen # Student ID: 6810545794

print("Enter coefficients for f(x) = ax^2 + bx + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print("\nEnter coefficients for g(x) = dx^2 + ex + f")
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))

print()
start = float(input("Enter the start of the interval (a): "))
end = float(input("Enter the end of the interval (b): "))
n = int(input("Enter the number of trapezoids (n): "))

if start >= end:
    print("\nError: The start of the interval must be less than the end.")
else:
    dx = (end - start) / n
    total_area = 0.0

    for i in range(n):
        x_i = start + i * dx
        x_next = x_i + dx

        f_xi = a * (x_i ** 2) + b * x_i + c
        g_xi = d * (x_i ** 2) + e * x_i + f
        diff_i = abs(f_xi - g_xi)

        f_next = a * (x_next ** 2) + b * x_next + c
        g_next = d * (x_next ** 2) + e * x_next + f
        diff_next = abs(f_next - g_next)

        trapezoid_area = ((diff_i + diff_next) / 2) * dx
        total_area += trapezoid_area

    print()
    print(f"Approximate area: {total_area:.6f}")
