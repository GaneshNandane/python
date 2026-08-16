class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("sound made by the animal")
class Dog (Animal):
    def __init__(self, name, bread):
        Animal.__init__(self, name, species = "Dog")
        self.bread = bread
    def make_sound(self):
        print("Bark!")
d = Dog("tommy", "bull dog")
d.make_sound()