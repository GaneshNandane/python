# simple tuple program and its operations and methods

# defining a tuple
tup=(1, 2, 76, 342, 32, "green",True)

# tuples are immutable so it does not support inserting a value 
# tup[0]=90

# printing the type of tuple as well as tuple 
print(type(tup),tup)

# printing the length of tuple
print(len(tup))

# printing the tuple value at index 0
print(tup[0])

# printing the last value of the tuple using negative indexing
print(tup[-1])

# printing the value at index 2 
print(tup[2])

# printing the value at index 34 which is not present in this tuple it shows us error saying out of index 
# print(tup[34])

# checking if the specific value in the tuple are present or not using conditional block 
if 342 in tup:
    print("Yes 342 is present in this tuple")

# creating a new tuple using existing tuple elements 
tup2=tup[1:4]

# printing the new tuple 
print(tup2)
