# in this program we are calculating the result of the two numbers by dividing both the numbers to each other 
# here we used the finally keyword it is similar to the else keyword
# note: finally keyword is always gets executed no matter what

try:
  value1 = int(input("Enter value1"))
  value2 = int(input("Enter value2"))
  result = value1/value2
except ZeroDivisionError:
  print("value can not be divided by the zero.")
except ValueError:
  print("value entered is not a valid value")
else:
  print("Result: ", result)
finally:
  print("Execution successful.")
