# try block code raise the in except block, valueerror if it is not an integer and prints the except block 
# then else block is get executed and finally block is get executed whether the condition is being executed from except of else 

try:
    num=int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")
