# Creating a Rectangle class with a constructor to initialize its width and height and Defining a class method named 'square' that acts as an alternative constructor
# to create a square by setting both the width and height to the same value.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def square(cls, size):
        return cls(size, size)

# Creating a square object with a side length of 10.
rectangle = Rectangle.square(10)

# Printing the width and height of the square.
print(rectangle.width)
print(rectangle.height)
