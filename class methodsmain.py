class Employee:
    Company = "Apple"
    def show(self):
        print(f"The name is {self.name} and Company is {self.Company}")
    @classmethod
    def changeCompany(cls, newCompany): 
        cls.Company = newCompany
e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.Company)
