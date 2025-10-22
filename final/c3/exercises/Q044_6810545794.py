# Name: Pasin Makcharoen # Student ID: 6810545794

import math

class Shape:
    def __init__(self, color):
        self.color = color
    
    def get_area(self):
        return self.color
    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        
    def get_area(self):
        area_ = math.pi * self.radius**2
        return area_
    
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
        
    def get_area(self):
        area_ = self.width * self.height
        return area_
    
class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height
    
    def get_area(self):
        area_ = 0.5 * self.base * self.height
        return area_
    

shapes_ = ["circle", "rectangle", "triangle"]

in_ = input("Create (circle/rectangle/triangle): ")
if in_ in shapes_:
    if in_ == "circle":
        col_ = input("Enter color: ")
        radi_ = float(input("Enter radius: "))

        this_ = Circle(col_, radi_)
        
        print(f"Info: Color: {col_}, Area: {this_.get_area():.2f}")
        
    elif in_ == "rectangle":
        col_ = input("Enter color: ")
        wid_ = float(input("Enter width: "))
        hei_ = float(input("Enter height: "))

        this_ = Rectangle(col_, wid_, hei_)

        print(f"Info: Color: {col_}, Area: {this_.get_area():.2f}")
            
    elif in_ == "triangle":
        col_ = input("Enter color: ")
        base_ = float(input("Enter base: "))
        hei_ = float(input("Enter height: "))

        this_ = Triangle(col_, base_, hei_)

        print(f"Info: Color: {col_}, Area: {this_.get_area():.2f}")
    
else:
    print("Invalid input")