# simple program to handle errors to avoid program being stop

# try block match the block with a valid data type if not it goes to except block and print whatever in the except block
try:
    num=int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
    
