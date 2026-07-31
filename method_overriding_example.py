# Base class
class Shape:
    # This method is meant to be overridden by child classes.
    # The 'pass' statement means there is no implementation here.
    def area(self):
        pass

# Child class for Circle
# This class inherits from Shape.
# The constructor (__init__) takes the radius as an argument
# and stores it in the instance variable 'radius'.
# The area() method calculates and returns the area of the circle.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Child class for Rectangle
# This class inherits from Shape.
# The constructor takes length and width as arguments
# and stores them in instance variables.
# The area() method calculates and returns the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Child class for Square
# This class inherits from Shape.
# The constructor takes the side length as an argument
# and stores it in the instance variable 'side'.
# The area() method calculates and returns the area of the square.
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Creating objects of each class
circle = Circle(5)
rectangle = Rectangle(10, 4)
square = Square(6)

# Calling the overridden area() method for each object
print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())
print("Area of Square:", square.area())
