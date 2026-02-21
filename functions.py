import math
a = int(input("Enter one number:"))
b = int(input("Enter another number:"))

# here we are calculating arithmetic mean in this block of code 
def calculateAmean(a, b):
  mean = (a + b)/2
  print("Aritmetic mean:",mean)
calculateAmean(a, b)

# here we are calculating geometric mean in this block of code
def calculateGmean(a, b):
  mean = math.sqrt(a * b)
  print("Geometric mean:",mean)
calculateGmean(a, b)
