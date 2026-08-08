# demonstrating private access modifiers in Python

# defining a Student class
class Student:

    # defining a constructor
    def __init__(self, age, name):

        # defining a private variable using double underscore
        self.__age = age

    # defining a private function using double underscore
    def __funName(self):

        # defining a variable
        self.y = 34

        # printing the value of y
        print(self.y)

# defining a Subject class that inherits from Student
class Subject(Student):
    pass

# creating an object of the Student class
obj = Student(21, "Harry")

# creating an object of the Subject class
obj1 = Subject()

# calling the private variable using the object of Student class
print(obj.__age)

# calling the private function using the object of Student class
print(obj.__funName())

# calling the private variable using the object of Subject class
print(obj1.__age)

# calling the private function using the object of Subject class
print(obj1.__funName())
