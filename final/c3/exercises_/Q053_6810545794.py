# Name: Pasin Makcharoen # Student ID: 6810545794

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.speed = 0
        
    def accelerate(self, amount):
        if amount > 0:
            self.speed += amount
            return f"{self.brand} accelerates."
        else:
            return None
        
    def brake(self, amount):
        if amount > 0:
            self.speed -= amount
            if self.speed < 0:
                self.speed = 0
            return f"{self.brand} brakes."
        else:
            return None
        
    def get_status(self):
        return f"{self.brand} Speed: {self.speed}"
        
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
        
        
vehicles = []
        
while True:
    in_reg = input("Register (car/motorcycle/done): ").lower()
    
    if in_reg == "done":
        print("--- Registered Vehicles ---")
        for i in vehicles:
            print(i.brand)
        print("---------------------------")
        break
    
    in_brad = input("Enter brand: ")
    in_yr = input("Enter year: ")

    if in_reg == "car":
        in_dors = input("Enter number of doors: ")
        this_car = Car(in_brad, in_yr, in_dors)
        
        vehicles.append(this_car)
        
        print("Vehicle added.")

    elif in_reg == "motorcycle":
        in_sid = input("Has sidecar (True/False): ")
        this_moto = Motorcycle(in_brad, in_yr, in_sid)
        
        vehicles.append(this_moto)
        
        print("Vehicle added.")

long_ = ["accel", "brake"]
short_ = ["status", "exit"]
invalid = "Invalid command."

all_v = [i.brand.lower() for i in vehicles]
# print(all_v)

while True:
    in_ = input("Enter command: ").strip().lower()
    
    if in_ == "":
        print(invalid)
    else:
        in_ = in_.split()
        
        if len(in_) > 3 or len(in_) == 2:
            print(invalid)
            continue
        
        if in_[0].lower() in long_ and len(in_) == 3:
            try:
                if in_[0].lower() == "accel":

                    if in_[1].lower() not in all_v:
                        print("Vehicle not found.")
                        continue

                    in_[2] = int(in_[2])

                    txts = []

                    for i in vehicles:
                        if i.brand.lower() == in_[1]:
                            a_ = i.accelerate(in_[2])
                            print(a_)
                        txts.append(f"Status: {i.get_status()}")
                    
                    print("\n".join(txts))

                elif in_[0].lower() == "brake":

                    if in_[1].lower() not in all_v:
                        print("Vehicle not found.")
                        continue

                    in_[2] = int(in_[2])

                    txts = []

                    for i in vehicles:
                        if i.brand.lower() == in_[1]:
                            a_ = i.brake(in_[2])
                            print(a_)
                        txts.append(f"Status: {i.get_status()}")
                    
                    print("\n".join(txts))
                
                else:
                    print(invalid)
                    continue

            except ValueError:
                print(invalid)
                continue


        elif in_[0].lower() in short_ and len(in_) == 1:
            if in_[0].lower() == "exit":
                print("Goodbye.")
                break
            
            elif in_[0].lower() == "status":
                for i in vehicles:
                    print(f"Status: {i.get_status()}")

        else:
            print(invalid)
            continue