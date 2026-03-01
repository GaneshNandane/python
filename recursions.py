# recursion is the function calling itself into that same function as it follws the condition rule it calls itself repeatedlly until a condition gets satisfied 
# Note: recursion uses stack memory so it is very easy to go out of memory storage or shorage of memory so you need to use it carfully

# so here is the working of the internal factorial function 
def factorial(n):
  """
  it does want a number as an input to calculate a factorial of that number
  you just enter the number that you want to multiply till one  
  then the function calls itself repeatedly until one 
  # 5 * factorial(4)
  # 5 * 4 * factorial(3)
  # 5 * 4 * 3 * factorial(2)
  # 5 * 4 * 3 * 2 * factorial(1)
  # 5 * 4 * 3 * 2 * 1 
  """
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5))
print(factorial.__doc__)
help(factorial)
