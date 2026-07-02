# demonstrating then use of class methods as a constructor 

class EmployeeClass:
    @classmethod
    def factory_method(cls, argument1, argument2):
        return cls(argument1, argument2)
