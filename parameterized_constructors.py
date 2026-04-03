# Python mainly has two types of constructors:

# 1. Default Constructor
#    - It takes only one argument called 'self'
#    - 'self' refers to the current object and binds the object to the class
#    - It is automatically called when an object is created
#    - It does not assign values unless explicitly written inside it

# 2. Parameterized Constructor
#    - It takes additional parameters along with 'self'
#    - These parameters are used to assign values to the object at the time of creation
#    - Each object gets its own values based on the arguments passed

# note: in this code we are discussing only parameterized constructors

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def PersonInfo(self):
    print(f"the name of the person is: {self.name}")
    print(f"the age of the person is: {self.age}")
    
p1 = Person("Ganesh", 21)
print(p1.name)
print(p1.age)
p1.PersonInfo()
