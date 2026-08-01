# Animal class
class Animal:

    # Constructor to initialize the animal's name and species
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Function to display the sound made by an animal
    def make_sound(self):
        print("Sound made by the animal")

# Mammal class
class Mammal:

    # Constructor to initialize the animal's name and fur color
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color

# Dog class inherits from both Animal and Mammal
# (Example of Multiple Inheritance)
class Dog(Animal, Mammal):

    # Constructor to initialize the dog's details
    def __init__(self, name, breed, fur_color):

        # Call the constructor of the Animal class
        Animal.__init__(self, name, species="Dog")

        # Call the constructor of the Mammal class
        Mammal.__init__(self, name, fur_color)

        # Store the dog's breed
        self.breed = breed

    # Overriding the make_sound() function of the Animal class
    def make_sound(self):
        print("Bark!")

# Creating an object of the Dog class
r = Dog("Tommy", "Bulldog", "Orange")

# Calling the overridden make_sound() function
print(r.make_sound())
