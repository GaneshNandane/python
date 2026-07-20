class MyClass:
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(self.name)
obj1 = MyClass("john")
obj2 = MyClass("Jane")

obj1.print_name()
obj2.print_name()
