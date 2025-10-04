# Name: Pasin Makcharoen # Student ID: 6810545794

import math

shapes = []

while True:
    in_ = input("Enter shape type (circle/rectangle/triangle) or 'done' to finish: ")

    if in_.lower() == "done":
        break

    if in_.lower() == "circle":
        r = input("Enter radius: ")
        area = math.pi * (float(r) ** 2)
        print(f"Circle area: {area:.2f}")
        shapes.append({"type": "Circle", "dimensions": f"radius {r}", "area": area})

    elif in_.lower() == "rectangle":
        w = input("Enter width: ")
        h = input("Enter height: ")
        area = float(w) * float(h)
        print(f"Rectangle area: {area:.2f}")
        shapes.append({"type": "Rectangle", "dimensions": f"width {w}, height {h}", "area": area})

    elif in_.lower() == "triangle":
        b = input("Enter base: ")
        h = input("Enter height: ")
        area = 0.5 * float(b) * float(h)
        print(f"Triangle area: {area:.2f}")
        shapes.append({"type": "Triangle", "dimensions": f"base {b}, height {h}", "area": area})

    else:
        print("Invalid shape type. Try again.")
    print()

print("\n--- SHAPE AREA REPORT ---")

total_area = sum(s["area"] for s in shapes)
print(f"Total area: {total_area:.2f}")

if shapes:
    largest = max(shapes, key=lambda s: s["area"])
    smallest = min(shapes, key=lambda s: s["area"])

    print(f"Largest shape: {largest['type']} with {largest['dimensions']}, area: {largest['area']:.2f}")
    print(f"Smallest shape: {smallest['type']} with {smallest['dimensions']}, area: {smallest['area']:.2f}")

print("-----------------------------")