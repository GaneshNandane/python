# Class representing a 3D vector
class Vector:

    # Constructor to initialize the vector components
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    # Overloading the str() function
    # This method is automatically called when the object is printed using the print() function.
    def __str__(self):
        # Return the vector in a readable mathematical format
        return f"{self.i}i + {self.j}j + {self.k}k"

    # Overloading the '+' operator
    # This method is called when two Vector objects are added.
    def __add__(self, x):
        # Create and return a new Vector whose components are the sum of the corresponding components of both vectors.
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)

# Create the first Vector object
v1 = Vector(3, 5, 6)

# Print the first vector
# Internally, Python calls: v1.__str__()
print(v1)

# Create the second Vector object
v2 = Vector(1, 2, 9)

# Print the second vector
print(v2)

# Add the two vectors using the overloaded '+' operator Internally, Python calls: v1.__add__(v2)
print(v1 + v2)

# Print the data type of the result returned by the '+' operator The result is a new Vector object.
print(type(v1 + v2))
