class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
class Dog(Animal):
    def __init__(self, name, bread):
        Animal.show_details(self)
        print(f"Bread: {self.bread}")
class GoldenRetriver(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, bread = "Golden Retriver")
        self.color = color
    def show_details(self):
        Dog.show_details(self)
        print(f"color: {self.color}")
