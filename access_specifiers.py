# python does not allow us to fully cover our variables and methods with strict access modifiers but it uses nameing conventions and name manglings 

# we can define
# private variables or methods as the __ in the begining of the variable or method 
# protected variables or methods as the _ in the begining of the variable or method 
# public variables or methods as the direct variable name or method instead of the __ or _ at the begining of the variables or the methods 

class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name          # public
        self._balance = balance   # protected
        self.__pin = pin          # private

    def show_balance(self):
        print("Balance:", self._balance)

    def deposit(self, amount):
        self._balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            self._balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Invalid PIN")

# Create object
acc = BankAccount("Ganesh", 10000, 1234)

# Public
print(acc.name)   

# Protected
print(acc._balance) 

# Private
# print(acc.__pin) 

# Access via methods
acc.show_balance()
acc.deposit(2000)
acc.withdraw(3000, 1234)

# Access private (not recommended)
print(acc._BankAccount__pin)  
