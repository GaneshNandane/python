# tuple in python are the build in data type which stores multiple values in a single tuple. tuples are ordered and unchangeable means that it is immutalbe in nature 
# tuple syntax
          # tuple_name = (value1, value2, value3, value4, ........)
# tuple syntax include tuple name followed by the assignment operator the round brackets inside round brackets value1, value2, value3, ..... so on 
# note : all values inside tuple must be seperated by quoma (,)

# single tuple example follwed by the string they do look similar but there is a large difference in the data type 
# example of string that is inside a round brackets with type funtion for knowing data type
tuple_of_single_item1 = ("Laptop")
print(type(tuple_of_single_item1))
print(tuple_of_single_item1)

# length of the string
print(len(tuple_of_single_item1))

# string index of the string
print(tuple_of_single_item1[0])
print(tuple_of_single_item1[1])

# checking if the letter L is in the string are prresent or not 
print("L" in tuple_of_single_item1)

# iterating over a string and printing the letters of the string
for i in tuple_of_single_item1:
  print(i)

# example of tuple with type funtion for knowing data type
tuple_of_single_item2 = ("Laptop",)
print(type(tuple_of_single_item2))
print(tuple_of_single_item2)

# length of the tuple
print(len(tuple_of_single_item2))

# tuple index of tuple
print(tuple_of_single_item2[0])
# print(tuple_of_single_item2[1])  # this gives error that the tuple index out of range

# iterating over a tuple and printing its elements of the tuple
for i in tuple_of_single_item2:
  print(i)


# tuple with the string values
tuple_of_items = ("Glass", "Bottel", "Watch", "Table",)
#                   [0]      [1]        [2]      [3]  

# printing the tuple
print(tuple_of_items)

# positive indexing of the tuple
print(tuple_of_items[0])
print(tuple_of_items[1])
print(tuple_of_items[2])
print(tuple_of_items[3])
# print(tuple_of_items[5]) # this gives error that the tuple index out or range

# neagtive indexing of the tuple
print(tuple_of_items[-1])
print(tuple_of_items[-2])
print(tuple_of_items[-3])
print(tuple_of_items[-4])
# print(tuple_of_items[-5]) # this gives errror that the tuple index out of range

# itereating over a tuple of items in an tuple and printing the values
for i in tuple_of_items:
  print(i)

# checking if the items in the tuple are present or not
if "Glass" in tuple_of_items:
  print("Glass is present")
else:
  print("Glass is absent")
  
# tuple with the number value
tuple_of_numbers = (23, 4, 64, 2, 8, 65, 83, 92, 10, 12,)
print(tuple_of_numbers)
 
# tuple with the string as well as the number value
tuple_of_mix_numbers_and_items = ("Glass", 5, "Bottel", "Watch", 54, 83, 10,)
print(tuple_of_mix_numbers_and_items)






  
  

