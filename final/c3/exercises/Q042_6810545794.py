# Name: Pasin Makcharoen # Student ID: 6810545794

class Motorcycle:
    def __init__(self):
        self.speed = 0
        self.mileage = 0
        
    def start(self):
        return "Motorcycle is starting..."
    
    def accelerate(self, amount):
        self.speed += amount
        return f"Accelerating... Current speed: {self.speed} km/h"
    
    def add_mileage(self, distance):
        if distance > 0:
            self.mileage += distance
            return None
        else:
            return None
        
    def stop(self):
        self.speed = 0
        return "Motorcycle has stopped."
    
    def get_status(self):
        return f"Current Speed: {self.speed} km/h, Total Mileage: {self.mileage} km"


bike = Motorcycle()
commands = ["start", "accel", "mileage", "stop", "status", "exit"]
invalid_ = "Invalid command. Please try again."
    
while True:
    in_ = input("Enter command: ").lower().strip().split()
    
    if len(in_) > 2 or len(in_) == 0:
        print(invalid_)
        continue
    elif len(in_) > 0:
        if in_[0] not in commands:
            print(invalid_)
            continue
        else:
            if in_[0] in ("accel", "mileage"):
                if len(in_) == 1:
                    print(invalid_)
                    continue
                else:
                    if in_[0] == "accel":
                        in_[1] = int(in_[1])
                        print(bike.accelerate(in_[1]))
                            
                    if in_[0] == "mileage":
                        in_[1] = int(in_[1])
                        bike.add_mileage(in_[1])
                        
            elif in_[0] in commands and len(in_) == 1 and in_[0] not in ("accel", "mileage"):
                if in_[0] == "start":
                    print(bike.start())
                        
                elif in_[0] == "stop":
                    print(bike.stop())
                        
                elif in_[0] == "status":
                    print(bike.get_status())
                        
                elif in_[0] == "exit":
                    print("Goodbye.")
                    break
                        
            else:
                print(invalid_)