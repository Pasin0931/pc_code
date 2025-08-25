def compute_and_display_real_roots(D, a, b):
    if D == 0:
        root = -b / (2 * a)
        print(f"One real root: {root:.3f}")
    else:
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Two real roots: {root1:.3f} and {root2:.3f}")

def compute_and_display_complex_roots(D, a, b):
    real_part = -b / (2 * a)
    imag_part = math.sqrt(-D) / (2 * a)
    print(f"Two complex roots: {real_part:.3f}+{-1 * imag_part:.3f}i and {real_part:.3f}{imag_part:.3f}i")

def solve_and_output(a, b, c):
    if a == 0:
        print("1st coefficient can't be zero. Program exits.")
        return
    D = b**2 - 4 * a * c
    if D >= 0:
        compute_and_display_real_roots(D, a, b)
    else:
        compute_and_display_complex_roots(D, a, b)

import math
a = float(input("Value of 1st coefficient: "))
if a == 0:
    print("1st coefficient can't be zero. Program exits.")
else:
    b = float(input("Value of 2nd coefficient: "))
    c = float(input("Value of 3rd coefficient: "))

    solve_and_output(a, b, c)
