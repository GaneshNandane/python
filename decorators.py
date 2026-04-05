# decorators in python is the way you can modify the functions so that you dont have to modify each of the function individually you just create a template like structure to be able to use before the function so that without  modifying the internal working of the function you just modify the function 
# note: decorators can be use to inhance the old codebases for the purpose of new meaningfull use without touching the original code 

# here the args and kwargs are:
#           1. args arguments mainlly positional arguments that is being stored inside tuple that is being explicitlly created at runtime
#           2. kwargs arguments mainlly are the key value argumnets that is being stored inside dictionary that is being explicitlly created at runtime

# this decorate function works as the template ford the other functions to be able to modify the function
def decorate(function):
  def decorate_from_both_side(*args, **kwargs):
    print("Hello this is the owner of the code")
    function(*args, **kwargs)
    print("Bye your function execution is successful")
  return decorate_from_both_side

# @decorate decorates the functionality of the function to print modification before and after the function call 
@decorate
def hello():
  print("Hello")

# @decorate decorates the functionality of the function to print modification before and after the function call 
@decorate
def multiply(a, b):
  print(a * b)

# this function calls are the modified one so that the output are get printed as the modified that is before and after some text are get printed according to the decoraters that are defined in this code
hello()
multiply(2, 4)
