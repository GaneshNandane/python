# Grandfather class (Base class)
class Grandfather:

    # Constructor to initialize the grandfather's name
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Father class inherits from Grandfather
class Father(Grandfather):

    # Constructor to initialize the father's name
    # and pass the grandfather's name to the Grandfather class
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        # Call the constructor of the Grandfather class
        Grandfather.__init__(self, grandfathername)

# Son class inherits from Father
class Son(Father):

    # Constructor to initialize the son's name
    # and pass the father's and grandfather's names
    # to the Father class
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname

        # Call the constructor of the Father class
        Father.__init__(self, fathername, grandfathername)

    # Function to display the names of all three generations
    def print_name(self):
        print("Grandfather name :", self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)

# Creating an object of the Son class
s1 = Son("Prince", "Rampal", "Lal mani")

# Printing the grandfather's name using the object
# (inherited attribute from the Grandfather class)
print(s1.grandfathername)

# Calling the function to print all family members' names
s1.print_name()
