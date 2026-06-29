# defining a function named greet that accepts any number of positional arguments using *args

def greet(*names):
    
# accessing the first three arguments and printing them 
    print("Hello,", names[0], names[1], names[2])
    
# passing three positional arguments to the function 
greet("James", "Buchanan", "Bornes")
