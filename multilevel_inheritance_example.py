# Base class representing a general animal
class Animal:

    # Constructor to initialize name and species
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Function to display animal details
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

# Dog class inherits from Animal
class Dog(Animal):

    # Constructor to initialize name and breed
    def __init__(self, name, breed):

        # Call the constructor of the Animal class
        Animal.__init__(self, name, "Dog")

        # Store the breed
        self.breed = breed

    # Function to display dog details
    def show_details(self):

        # Call Animal's show_details() function
        Animal.show_details(self)

        # Print breed
        print(f"Breed: {self.breed}")

# GoldenRetriever class inherits from Dog
class GoldenRetriever(Dog):

    # Constructor to initialize name and color
    def __init__(self, name, color):

        # Call the constructor of Dog class
        Dog.__init__(self, name, "Golden Retriever")

        # Store color
        self.color = color

    # Function to display all details
    def show_details(self):

        # Call Dog's show_details() function
        Dog.show_details(self)

        # Print color
        print(f"Color: {self.color}")

# Creating an object of GoldenRetriever
dog1 = GoldenRetriever("Buddy", "Golden")

# Calling the function
dog1.show_details()
