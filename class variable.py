class MyClass:
    Class_variable = 0
    
    def __init__(self):
        MyClass.Class_variable +=1
    def print_Class_variable(self):
        print(MyClass.Class_variable)
obj1 = MyClass()
obj2 = MyClass()

obj1.print_Class_variable()
obj2.print_Class_variable()