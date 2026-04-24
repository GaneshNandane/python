# inheritance is the thing in python that follows the traits of it's parent class in the next class when it's defined out of that class
# there are multiple inheritance are present 
          # Single inheritance
          # Multiple inheritance
          # Multilevel inheritance
          # Hierarchical Inheritance
          # Hybrid Inheritance

# here we are applying the hybrid one that is the combination of the all other inheritance 

# Base class
class Account:
    def deposit(self):
        print("Money deposited")

# Derived class 1
class Savings(Account):
    def interest(self):
        print("Interest applied")

# Derived class 2
class Loan(Account):
    def loan(self):
        print("Loan facility available")

# Hybrid class
class PremiumAccount(Savings, Loan):
    def premium_feature(self):
        print("Premium benefits enabled")

# Object
acc = PremiumAccount()

acc.deposit()         
acc.interest()        
acc.loan()            
acc.premium_feature() 
