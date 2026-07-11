# template for hirarchical inheritance 

# class 1
# it is a base class or a parent class 
class BaseClass:
    pass

# class 2
# it is child class inherited from the base class or parent class 
class D1(BaseClass):
    pass

# class 3
# it is child class inherited from the base class  or parent class above this class 
class D2(BaseClass):
    pass

# class 4
# it is child class inherited from the base class  or parent class above this class 
class D3(D1):
    pass
