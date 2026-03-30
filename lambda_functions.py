# lambda is a special keyword used to create a small functions with single expression that works similar to the normal function

# here is the function that is used to add another function with value of 6 adding to the existing new function

def appl(fx, value):
  return 6 + fx(value)

# function for double the value 
double = lambda x: x * 2

# function for cube the value 
cube = lambda x: x * x * x

# function for average of the value 
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))

# this is the function call where there is two arguments first one is another function and second one is value 
      # lambda x: x * x is one argument which is function
      # 2 is second argument which is a value 
print(appl(lambda x: x * x , 2))
