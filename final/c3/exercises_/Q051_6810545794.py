# Name: Pasin Makcharoen # Student ID: 6810545794

class CoffeeMachine:
    def __init__(self, water: int, beans: int):
        self.__water_level = water
        self.__beans_level = beans
        
    def __grind_beans(self):
        if self.__beans_level - 10 < 0:
            return None
        else:
            self.__beans_level -= 10
            return "Grinding coffee beans..."
        
    def __heat_water(self):
        if self.__water_level - 20 < 0:
            return None
        else:
            self.__water_level -= 20
            return "Heating water..."
        
    def __pour_espresso(self):
        return "Pouring espresso shot..."
    
    def make_espresso(self):
        if self.__water_level >= 20 and self.__beans_level >= 10:
            m_1 = self.__heat_water()
            m_2 = self.__grind_beans()
            m_3 = self.__pour_espresso()
            
            return [m_1, m_2, m_3, "Your espresso is ready!"]
        else:
            return ["Error: Please refill water or beans."]
        
    def get_status(self):
        return f"Water: {self.__water_level}, Beans: {self.__beans_level}"
    
    
in_wa = int(input("Enter initial water level: "))
in_bea = int(input("Enter initial beans level: "))

maker_ = CoffeeMachine(in_wa, in_bea)

while True:
    in_ = input("Enter command (make/status/exit): ").strip().lower()
    
    if in_ == "exit":
        print("Goodbye.")
        break
    
    elif in_ == "make":
        msgs = maker_.make_espresso()
        for i in msgs:
            print(i)
            
    elif in_ == "status":
        print(maker_.get_status())