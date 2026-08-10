class Student:
    def __init__(self):
        self._name = "Harry"
    def _funName(self):         #Protected Method
        return "CodeWithHarry"
class Subject(Student):         #inherited class
    pass
obj = Student()
obj1 = Subject()

# calling by object of student class
print(obj._name)
print(obj._funName())

#calling by object of subject class
print(obj1._name)
print(obj1._funName())