# Class representing the details of an animal
class Details:

    # Parameterized constructor
    # It accepts two arguments (animal and group) along with 'self' to initialize the object's attributes when it is created.
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

# Create an object of the Details class.
# The values "Crab" and "Crustaceans" are passed to the parameterized constructor to initialize the object's attributes.
obj1 = Details("Crab", "Crustaceans")

# Print the values stored in the object's attributes.
print(obj1.animal, "belongs to the", obj1.group, "group.")
