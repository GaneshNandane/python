# this is the definition of the class and it's methods which is being used inside the dunder_methods_main.py
# it can be imported to that file and can be used 

class Employee:

    # this is the constructor which is being called automatically called when we create an object of this class inside the new file which is in this case dunder_methods_main.py  
    def __init__(self, name):
        self.name = name

    # it is a special method which calculate the length of the object as defined by this method when it is being used inside the dunder_methods_main.py 
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    # it is a special method which is used to print the user friendly string representation of the object inside the dunder_methods_main.py when being called inside it 
    def __str__(self):
        return f"The name of the Employee is {self.name} str"

    # it is a special method which prints the formated employee object inside dunder_methods_main.py when being called inside it 
    def __repr__(self):
        return f"Employee ('{self.name}')"

    # it is a special method which is being used when the object is being used as an function inside dunder_methods_main.py when being called inside it 
    def __call__(self):
        print("Hey i am good")
