x=10 #global variable 
def my_function():
    global x
    x=5 # this will change the vlaue of the global variable x
    # this is the local variable this is limited to this function we can only use this variable within this function 
    y=5 #local variable 
    print(y)
my_function()
print(x) #prints 5
# print(y) #this will cause and error because y is a local variable and is not accessible outside of the function
