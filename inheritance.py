# Inheritance in Python allows a class (child class) 
# to inherit properties and methods from another class (parent class).

# Types of inheritance in Python:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

# Hybrid inheritance is a combination of two or more types 
# of inheritance (for example: hierarchical + multiple).

# Base class
class Account:
    def deposit(self):
        print("Money deposited")

# Derived class 1 (Hierarchical inheritance)
class Savings(Account):
    def interest(self):
        print("Interest applied")

# Derived class 2 (Hierarchical inheritance)
class Loan(Account):
    def loan(self):
        print("Loan facility available")

# Hybrid class (Multiple inheritance + Hierarchical)
class PremiumAccount(Savings, Loan):
    def premium_feature(self):
        print("Premium benefits enabled")

# Creating object of hybrid class
acc = PremiumAccount()

# Accessing methods from different classes
acc.deposit()         # inherited from Account
acc.interest()        # inherited from Savings
acc.loan()            # inherited from Loan
acc.premium_feature() # method of PremiumAccount
