# static methods in python are the methods that works like any other methods but it is defined inside the class using the @staticmethod 
# this method does not depend on the class instance if we create a class instance or not create it still works fine 
# Note : you can define multiple static methods inside a single class

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance method
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

    # Static method
    @staticmethod
    def calculate_grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 50:
            return "C"  
        else:
            return "Fail"


# Creating objects
s1 = Student("Ganesh", 85)
s2 = Student("Rahul", 45)

# Using instance method
s1.display()
s2.display()

# Using static method
print("Grade:", Student.calculate_grade(85))
print("Grade:", Student.calculate_grade(45))
