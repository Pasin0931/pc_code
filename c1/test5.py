def read_multiple_inputs():
    s1 = read_one_input("Enter length of side1: ")
    s2 = read_one_input("Enter length of side2: ")
    s3 = read_one_input("Enter length of side3: ")
    return s1, s2, s3

def read_one_input(text):
    input_v = float(input(text))
    return input_v

def calculate_tri_perimeter(s1, s2, s3):
    return s1 + s2 + s3

def calculate_tri_area(s, a, b ,c):
    s = s / 2
    val = s * (s - a) * (s - b) * (s - c)
    return math.sqrt(val)

def display_all_outputs(ob1, ob2, ref1, ob3, ref2):
    print(f"The {ob2} of {ob1} is {ref1:.2f}")
    print(f"The {ob3} of {ob1} is {ref2:.2f}")

import math
a,b,c = read_multiple_inputs()
s = calculate_tri_perimeter(a,b,c)
area = calculate_tri_area(s,a,b,c)
display_all_outputs("triangle", "perimeter", s, "area", area)