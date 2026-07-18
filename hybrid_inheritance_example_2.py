# this is a hybrid inheritance program 
# here we have four classes that is forming a struncture of hybrid inheritance 

# Parent class
class Human:

    # Constructor to initialize the name and age of a human
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display the human's details
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Person class inherits from Human (Multilevel Inheritance starts here)
class Person(Human):

    # Constructor to initialize name, age, and address
    def __init__(self, name, age, address):

        # Calling the constructor of the Human class
        Human.__init__(self, name, age)

        # Person-specific attribute
        self.address = address

    # Overriding the show_details() method
    def show_details(self):

        # Calling the parent class method
        Human.show_details(self)

        # Displaying the address
        print("Address:", self.address)

# Separate class to represent a study program
class Program:

    # Constructor to initialize the program name and duration
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration

    # Method to display program details
    def show_details(self):
        print("Program Name:", self.program_name)
        print("Duration:", self.duration, "Years")

# Student class inherits from Person (Multilevel Inheritance)
class Student(Person):

    # Constructor to initialize student details
    def __init__(self, name, age, address, program):

        # Calling the constructor of the Person class
        Person.__init__(self, name, age, address)

        # Storing a Program object inside the Student object
        # This demonstrates Composition (Has-A relationship)
        self.program = program

    # Overriding the show_details() method
    def show_details(self):

        # Displaying the inherited details
        Person.show_details(self)

        # Displaying the details of the Program object
        self.program.show_details()

# Creating an object of the Program class
program = Program("Computer Science", 4)

# Creating an object of the Student class
# The student "has a" Program object
student = Student("John Doe", 25, "123 Main St.", program)

# Displaying all the student details
student.show_details()
