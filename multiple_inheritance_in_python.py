# Mother class
class Mother:

    # Class variable to store the mother's name
    mothername = " "

    # Function to display the mother's name
    def mother(self):
        print(self.mothername)

# Father class
class Father:

    # Class variable to store the father's name
    fathername = " "

    # Function to display the father's name
    def father(self):
        print(self.fathername)

# Son class inherits from both Mother and Father
# (Example of Multiple Inheritance)
class Son(Mother, Father):

    # Function to display the names of both parents
    def parents(self):
        print("Father name is:", self.fathername)
        print("Mother name is:", self.mothername)

# Creating an object of the Son class
s1 = Son()

# Assigning the father's name
s1.fathername = "Daddy"

# Assigning the mother's name
s1.mothername = "Mommy"

# Calling the function to display both parents' names
s1.parents()
