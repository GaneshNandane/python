# Python mainly has two types of constructors:

# 1. Default Constructor
#    - It takes only one argument called 'self'
#    - 'self' refers to the current object and binds the object to the class
#    - It is automatically called when an object is created
#    - It does not assign values unless explicitly written inside it

# 2. Parameterized Constructor
#    - It takes additional parameters along with 'self'
#    - These parameters are used to assign values to the object at the time of creation
#    - Each object gets its own values based on the arguments passed

# Note: In this code, we are only discussing the default constructor

class message:
    def __init__(self):
        print("This is the default constructor")

p1 = message()
