# Name: Pasin Makcharoen # Student ID: 6810545794

import math

shapes = []
t_area = []

while True:
    in_ = input("Enter shape type (circle/rectangle/triangle) or 'done' to finish: ")

    if in_ == "done":
        break

    if in_ == "circle":
        try:
            r = input("Enter radius: ")
            r_float = float(r)
            area = math.pi * (r_float ** 2)
            print(f"Circle area: {area:.2f}")
            shapes.append({"type": "Circle", "dimensions": f"radius {r}", "area": area})
            t_area.append(f"{area:.2f}")
        except ValueError:
            print("Invalid radius entered. Please enter a number.")

    elif in_ == "rectangle":
        try:
            w = input("Enter width: ")
            h = input("Enter height: ")
            w_float = float(w)
            h_float = float(h)
            area = w_float * h_float
            print(f"Rectangle area: {area:.2f}")
            shapes.append({"type": "Rectangle", "dimensions": f"width {w}, height {h}", "area": area})
            t_area.append(f"{area:.2f}")
        except ValueError:
            print("Invalid width or height entered. Please enter numbers.")

    elif in_ == "triangle":
        try:
            b = input("Enter base: ")
            h = input("Enter height: ")
            b_float = float(b)
            h_float = float(h)
            area = 0.5 * b_float * h_float
            print(f"Triangle area: {area:.2f}")
            shapes.append({"type": "Triangle", "dimensions": f"base {b}, height {h}", "area": area})
            t_area.append(f"{area:.2f}")
        except ValueError:
            print("Invalid base or height entered. Please enter numbers.")

    else:
        print("Invalid shape type. Try again.")
    print()

print("\n--- SHAPE AREA REPORT ---")

total_area = sum(s["area"] for s in shapes)

t_area = list(map(float, t_area))

print(f"Total area: {sum(t_area):.2f}")

if shapes:
    largest = max(shapes, key=lambda s: s["area"])
    smallest = min(shapes, key=lambda s: s["area"])

    # print(largest)
    # print(smallest)

    print(f"Largest shape: {largest['type']} with {largest['dimensions']}, area: {largest['area']:.2f}")
    print(f"Smallest shape: {smallest['type']} with {smallest['dimensions']}, area: {smallest['area']:.2f}")

print("-----------------------------")