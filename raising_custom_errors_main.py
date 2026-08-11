# this is the simple example of raising a custom error

# in this example we are raising a custom error for values that are other that 5 and 9 inbetween
a=int(input("Enter any value between 5 and 9: "))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")
