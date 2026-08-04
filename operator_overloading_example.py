# Class representing a point in a 2D coordinate system
class Point:

    # Constructor to initialize x and y coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    # This method is automatically called when two Point objects are added using the '+' operator.
    def __add__(self, other):
        # Create and return a new Point object whose coordinates are the sum of the corresponding coordinates of both objects.
        return Point(self.x + other.x, self.y + other.y)

# Create the first Point object
P1 = Point(1, 2)

# Create the second Point object
P2 = Point(3, 4)

# Add the two Point objects using the overloaded '+' operator Internally, this calls: P1.__add__(P2)
P3 = P1 + P2

# Print the coordinates of the resulting Point object
print(P3.x, P3.y)
