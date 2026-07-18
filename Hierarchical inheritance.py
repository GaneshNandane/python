class Animal:
    def __init__(self, name):
        self.name = name
    def show_details(self):
        print("Name:", self.name)
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed 
    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)
class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color
    def show_details(self):
        Animal.show_details(self)
        print("Species: cat")
        print("color: ", self.color)
dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()