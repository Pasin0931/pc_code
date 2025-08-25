# def read_trapezoid():
#     print("Specify the properties of your trapezoid.")
#     s1 = float(input("Enter length of parallel side 1: "))
#     s2 = float(input("Enter length of parallel side 2: "))
#     h = float(input("What is the height? "))
#     return s1, s2, h

# def trapezoid_area(s1, s2, h):
#     return ((s1 + s2) / 2) * h

# side1, side2, height = read_trapezoid()
# area = trapezoid_area(s2=side2, h=height, s1=side1)
# print(f"The trapezoid area is {area:.2f}")

# -------------------

# def compute_work(force, dist=1, angle=0):
#     from math import cos, radians
#     return force * dist * cos(radians(angle))

# print(compute_work(15, dist=20))
# print(compute_work(15, angle=120))