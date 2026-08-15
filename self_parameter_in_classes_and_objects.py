# simple program to demonstrate the use of self parameter

# defining a class with class variables and class methods
class Details:
    # defining class variables
    name="Rohan"
    age=20

    # defining class methods with self parameter
    # self use to define the current object data to the class methods
    def desc(self):
        print("My name is",self.name,"and i'm",self.age,"years old")

# creating object of Details class 
obj1=Details()

# calling the instance method using class object
obj1.desc()
