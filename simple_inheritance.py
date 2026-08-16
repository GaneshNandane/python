# Simple program to demonstrate single inheritance and method overriding

# Define the parent class Animal
class Animal:

    # Define the constructor to initialize the name and species of the animal
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Define an instance method to make a general animal sound
    def make_sound(self):
        print("Sound made by the animal")

# Define the child class Dog that inherits from the Animal class
class Dog(Animal):

    # Define the constructor to initialize the dog's name and breed
    def __init__(self, name, breed):

        # Call the parent class constructor to initialize the inherited attributes
        Animal.__init__(self, name, species="Dog")

        # Store the dog's breed in the breed attribute
        self.breed = breed

    # Override the parent class make_sound() method for the Dog class
    def make_sound(self):
        print("Bark!")

# Create an object of the Dog class with its name and breed
d = Dog("Tommy", "Bulldog")

# Call the overridden make_sound() method of the Dog object
d.make_sound()
