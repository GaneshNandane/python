# simple program to demonstrate the use of simple inheritance

# defining a parent class Animal
class Animal:
    # defining a constructor with two arguments for parent class
    def __init__(self, name, species):
        self.name = name
        self.species = species
    # defining a parent class method 
    def make_sound(self):
        print("sound made by the animal")

# defining the child class of parent class the child class is inherited from the Animal class
class Dog (Animal):
    # defining a constructor with two arguments for child class 
    def __init__(self, name, bread):

        # extracting the parent class variables to the child class using parent class constructor
        Animal.__init__(self, name, species ="Dog")
        self.breed = breed
        
    # defining a child class method
    def make_sound (self):
        print("Bark!")

# creating the object of child class with two arguments
d = Dog ("Dog", "Doggerman")

# calling the instane method of child class 
d.make_sound()

# creating the object of parent class with two arguments
a = Animal("Dog", "Dog")

# calling the instance methods of parent class 
a.make_sound()
