# Name: Pasin Makcharoen # Student ID: 6810545794

class Dog:
    def __init__(self):
        pass
    def speak(self):
        return "Woof!"
    
class Cat:
    def __init__(self):
        pass
    def speak(self):
        return "Meow!"
    
class Robot:
    def __init__(self):
        pass
    def speak(self):
        return "Beep Boop!"
    
all_ = ["dog", "cat", "robot"]

while True:
    in_ = input("Create (dog/cat/robot/exit): ").lower()

    if in_ == "exit":
        print("Goodbye.")
        break

    elif in_ == "dog":
        this_ = Dog()

    elif in_ == "cat":
        this_ = Cat()

    elif in_ == "robot":
        this_ = Robot()

    else:
        print("Invalid input.")
        continue

    print(this_.speak())