# Name: Pasin Makcharoen # Student ID: 6810545794

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors
        
    def return_sts(self):
        return f"Registered: Brand: {self.brand}, Year: {self.year}, Doors: {self.num_doors}"
        
class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar
        
    def return_sts(self):
        return f"Registered: Brand: {self.brand}, Year: {self.year}, Sidecar: {self.has_sidecar}"
        
in_reg = input("Register (car/motorcycle): ").lower()
in_brad = input("Enter brand: ")
in_yr = input("Enter year: ")

if in_reg == "car":
    in_dors = input("Enter number of doors: ")
    this_car = Car(in_brad, in_yr, in_dors)
    
    print(this_car.return_sts())

elif in_reg == "motorcycle":
    in_sid = input("Has sidecar (True/False): ")
    this_moto = Motorcycle(in_brad, in_yr, in_sid)
    
    print(this_moto.return_sts())