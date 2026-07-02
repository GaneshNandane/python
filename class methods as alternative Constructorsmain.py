class Employee:
    def __init__(self, name, Salary):
        self.name = name
        self.Salary = Salary  
    @classmethod
    def fromStr(cls, String):
        return cls (String.split("-")[0]), int(String.split("-")[1])
e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.Salary)
String = "john-12000"
e2 = Employee.fromStr(String)
print(e2.name)
print(e2.Salary)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, String):
        name, age = String.split(',')
        return cls(name, int(age))
person = Person.from_string("John Doe, 30")
print(person.name, Person.age)