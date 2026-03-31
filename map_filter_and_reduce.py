from functools import reduce

# syntax for map 
      # map(function, i  terable)

# the map function have  two  areguments a function and a list of integers function performs an operation on a list and returns the iterators after performing operation on the list we need to convert the iterator into the list 
  # here in this case we are squaring all elements inside a list 
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = map(lambda x: x**2, numbers1)
print(list(squared))
  
# syntax for filter 
      # filter(function, iterable)

# the filter function have two arguments a function and a list of integers function performs an operation such that some of the values are get filtered on the way and returns iterators on to the console and we need to convert the iterator into the list
  # here in this case we are extracting the values that are only the multiple of three inside a list 
numbers2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

multiple_of_three = filter(lambda x: x % 3 == 0, numbers2)
print(list(multiple_of_three))

# syntax for reduce
      # reduce(function, iterable)

# the reduce function have two arguments a function and a list of integers function performs an operation on the existing list in such way that it reduces the the existing list into a single value and prints the value to the consle
  # here in this case we are adding all the values that are present inside the list 
numbers3 = [1, 3, 6, 9, 12, 15, 18, 21, 24]

sum_all = reduce(lambda x, y: x + y, numbers3)
print(sum_all)
