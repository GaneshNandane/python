#Example of hybrid inheritance

# class 1 
# this is a base class or a parent class  
class BaseClass:
    pass

# class 2 
# this is derived class from the upper base class or parent class
class Derived1 (BaseClass):
    pass

# class 3 
# this is derived class from the upper base class or parent class
class Derived2(BaseClass):
    pass

# class 4 
# this is derived class from the upper base class or parent class
class Derived3(Derived1, Derived2):
    pass
