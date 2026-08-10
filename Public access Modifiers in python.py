class Student:
    #constructor is defined
    def __init__(self, age, name):
        self.age = age      #Public Variable
        self.name = name    #Public Variable
obj = Student(21, "Harry")
print(obj.age) 
print(obj.name)       
        
