# Constructor initialization in a class

# In this program, we define a class named Person. The class method info() displays the information of each Person object.
# The constructor (__init__) is called automatically whenever an object is created. It initializes the object's attributes (name and occupation) using the values
# passed during object creation so that they can be used by other class methods. Note: Each object has its own separate set of instance attributes stored in memory.

class Person:
  
  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")

# object creation one
a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
a.info()
b.info()

# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()
