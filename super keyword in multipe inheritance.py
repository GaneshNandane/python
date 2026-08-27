class ParentClass1:
    def Parent_method(slef):
        print("This is the parent method of ParentClass1.")
class ParentClass2:
    def parent_method(self):
        print("This is  the parent method of ParentClass2.")
class ChildClass(ParentClass1, ParentClass2):
    def Child_method(self):
        print("This is the Child method.")
        super().parent_method()
Child_object = ChildClass()
Child_object.Child_method()