class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("Sound made by the animal")
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
class Dog(Animal, Mammal):
    def __init__(self, name, bread, fur_color):
        Animal.__init__(self, name, species = "Dog")
        Mammal.__init__(self, name, fur_color)
        self.bread = bread
    def make_sound(self):
        print("Bark!")
r = Dog ("tommy", "bullDog", "orange")
print(r.make_sound())