# this is the example of the hierarchical inheritance 

# Parent class
class Animal:

    # Constructor of the parent class
    def __init__(self, name):
        self.name = name

    # Method to display the animal's name
    def show_details(self):
        print("Name:", self.name)

# Child class Dog inheriting from Animal
class Dog(Animal):

    # Constructor of Dog class
    def __init__(self, name, breed):

        # Calling the constructor of the parent class
        Animal.__init__(self, name)

        # Dog-specific attribute
        self.breed = breed

    # Overriding the show_details() method
    def show_details(self):

        # Calling the parent class method
        Animal.show_details(self)

        # Displaying additional Dog information
        print("Species: Dog")
        print("Breed:", self.breed)

# Child class Cat inheriting from Animal
class Cat(Animal):

    # Constructor of Cat class
    def __init__(self, name, color):

        # Calling the constructor of the parent class
        Animal.__init__(self, name)

        # Cat-specific attribute
        self.color = color

    # Overriding the show_details() method
    def show_details(self):

        # Calling the parent class method
        Animal.show_details(self)

        # Displaying additional Cat information
        print("Species: Cat")
        print("Color:", self.color)

# Creating an object of Dog class
dog = Dog("Max", "Golden Retriever")

# Calling the overridden method
dog.show_details()

print()  # Blank line for better output formatting

# Creating an object of Cat class
cat = Cat("Luna", "Black")

# Calling the overridden method
cat.show_details()
