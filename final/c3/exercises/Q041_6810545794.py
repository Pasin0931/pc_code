# Name: Pasin Makcharoen # Student ID: 6810545794

class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self._name = name
        self.__major = major
        
        self.credits = 0
        
    def get_info(self):
        return f"ID: {self.student_id}, Name: {self._name}, Major: {self.__major}, Credits: {self.credits}"
    
id_ = input("Enter student ID: ")
name_ = input("Enter name: ")
major_ = input("Enter major: ")

s1 = Student(id_, name_, major_)

print(s1.get_info())