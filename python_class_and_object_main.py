# Defining a Person class
class Person:

    # Defining class attributes
    name = "Harry"
    occupation = "Software Developer"
    networth = 10

    # Defining a method to display the person's information
    def info(self):
        print(f"{self.name} is a {self.occupation}")

# Creating three objects of the Person class
a = Person()
b = Person()
c = Person()

# Changing the name and occupation of object a
a.name = "Shubham"
a.occupation = "Accountant"

# Changing the name and occupation of object b
b.name = "Nitika"
b.occupation = "HR"

# Calling the info method for each object
a.info()
b.info()
c.info()
