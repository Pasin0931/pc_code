# # class Car:
# #     def __init__(self, name, speed_now):
# #         self.name = name
# #         self.speed_now = speed_now
        
# #     def getSpeed(self):
# #         return self.speed_now
    
# #     def getName(self):
# #         return self.name
    
# #     def changeSpeed(self, val):
# #         self.speed_now = val
# #         return f"Current speed {self.speed_now}"
    
# # car1 = Car("Nissan", 10)

# # print(car1.getSpeed())
# # print(car1.getName())

# # print(car1.changeSpeed(20))

# # print(car1.changeSpeed(1000))

# # print(car1.getSpeed())


# class Human:
#     def __init__(self, name, speak_):
#         self.name = name
#         self.speak_ = speak_
    
#     def getName(self):
#         return self.name
    
#     def setName(self, new_name):
#         self.name = new_name
#         return f"Name changed to {new_name}"
    
#     def speaking(self):
#         return f"{self.name} is speaking . . . '{self.speak_}'"
    
# class Asian(Human):
#     def __init__(self, name, speak_, iq):
#         super().__init__(name, speak_)
#         self.iq = iq
        
#     def getIq(self):
#         return self.iq
    
#     def setIq(self, newIq):
#         self.iq = newIq
#         return f"{self.name} IQ chnged to {newIq}"
    
# class abc(Human):
#     def __init__(self, name, speak_, is_violence=True):
#         super.__init__(name, speak_)
        
#         if type(self.is_violence) != bool:
#             self.is_violence = True
#         else:
#             self.is_violence = is_violence
        
#     def check_violence(self):
#         return self.is_violence
    
#     def set_violence(self, status_):
#         if type(status_) != bool:
#             self.is_violence = True
#         else:
#             self.is_violence = status_
        
#         if status_ == True:
#             return f"Change status to violence\nDeporting this nigga . . ."
#         else:
#             return f"Change status to non-violence"
        
# sapian_1 = Human("Adam", "Hello people")
# print(sapian_1.getName())
# print(sapian_1.setName("Paul"))
# print(sapian_1.speaking())
