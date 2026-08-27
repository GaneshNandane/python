# Simple program to demonstrate the use of the super() function
# with method overriding

# Define the parent class
class Shape:

    # Define a method to calculate the area
    def area(self):
        print("Calculating area .....")

# Define the child class that inherits from Shape
class Circle(Shape):

    # Define a constructor that accepts the radius of the circle
    def __init__(self, radius):
        self.radius = radius

    # Override the area() method of the parent class
    def area(self):
        print("Calculating area of a circle ....")

        # Call the area() method of the parent class using super()
        super().area()

        # Calculate and return the area of the circle
        return 3.14 * self.radius * self.radius
    
