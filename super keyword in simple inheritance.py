class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        super().parent_method()
        print("This is the child method.")
child_object = ChildClass()
child_object.child_method()
