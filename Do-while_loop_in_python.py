# implementing a do-while loop in python 

# Note: it will execute at once 
# seting the condition to True 
while True:
    # taking user input as a number 
    number = int(input("Enter a positive number"))

    # printing that number until the if condition gets satisfied 
    print(number)

    # checking if the number is 0 or negative if it is then the loop get imidiatelly break 
    if not number>0:
        break
