class Student:

    # Defining the constructor to initialize the object
    def __init__(self, age, name):

        # Defining public variables
        self.age = age
        self.name = name

# Creating an object of the Student class
obj = Student(21, "Harry")

# Accessing the public variables directly using the object
print(obj.age)
print(obj.name)

      
        
