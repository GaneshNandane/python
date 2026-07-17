# Parent class
class Parent:

    # Method of the parent class
    def func1(self):
        print("This function is in Parent class.")

# First child class inheriting from Parent
class Child1(Parent):

    # Method of Child1
    def func2(self):
        print("This function is in Child1.")

# Second child class inheriting from Parent
class Child2(Parent):

    # Method of Child2
    def func3(self):
        print("This function is in Child2.")

# Creating an object of Child1
object1 = Child1()

# Creating an object of Child2
object2 = Child2()

# Calling the inherited method from Parent
object1.func1()

# Calling Child1's own method
object1.func2()

# Calling the inherited method from Parent
object2.func1()

# Calling Child2's own method
object2.func3()
