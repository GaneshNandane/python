# here it is a custom error that tells us if the entered value is between 5 and 9

class RangeError(Exception):
  pass
number = int(input("Enter any value: "))
if number < 5 or number > 9:
  raise RangeError("Value should be between 5 and 9")
