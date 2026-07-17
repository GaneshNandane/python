class parent:
    def func1(self):
        print("This function is in parent class.")
class Child1(parent):
    def func2(slef):
        print("This function is in Child1.")
class Child2(parent):
    def func3(self):
        print("This function is in Child2")
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()