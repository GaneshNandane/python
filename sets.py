# sets are the one of the data type which is build in data type in python
# sets are the unordered unindexed collection of values 
# note: the values in sets are not duplicate or sets exced the values that are duplicates 

# sytax of the sets
# sets are defined by the set name followed by the assignment operator and curlly braces with each value seperated by the quoma (,)
          # set_name = {value1, value2, value3, value4, ........}

# example of set
my_set1 = {2, 2, 3, 1, 65, 2, 6, 78, 2, 8, 4, 8, 56, "set", "tree", "forse"}
my_set2 = {3, 3, 5, 6, 8, 3, 8, 3, 2, 1, "fan", "light"}
my_set3 = {5, 35,37, 23, 83, 83, 18, 19, 23}


# printing the the type of the set variable my_set1
print(type(my_set1))

# printing the values that are present in the my_set1
print(my_set1)

# printing length of the set
print(len(my_set1))

# it is possible to use the set constructor to make the set
my_set4 = set()
print(type(my_set4))

# adding elements to the exosting set
my_set1.add("help")
print(my_set1)

# updateing the multiple elements into the set
# note: update method works with multiple build in data types like list tuple or another sets
my_set1.update((12, 53, 75, 29))
print(my_set1)

# removeing the perticular element from the set but it gives errror if the element is not present in the set
my_set1.remove("help")
print(my_set1)

# it removes the perticluar element from the set wihtout geting error if the element is not prsent in the set
my_set1.discard(78)
print(my_set1)

# pop removes the random element from the set
my_set1.pop()
print(my_set1)

# clear removes all elements from the set
my_set3.clear()
print(my_set3)

# it prints the combined sets
# note: both below methods works the same way 
print(my_set1.union(my_set2))
print(my_set1 | my_set2)

# prints common elements in the set
# note: both below methods works the same way 
print(my_set1.intersection(my_set2))
print(my_set1 & my_set2)

# prints elements in the first set but not the second set
# note: both below methods works the same way 
print(my_set1.difference(my_set2))
print(my_set1 - my_set2)

# prints elements from the both sets except common elements
# note: both below methods works the same way 
print(my_set1.symmetric_difference(my_set2))
print(my_set1 ^ my_set2)

# createing the copy of the existing set
my_new_set = my_set1.copy()
print(my_new_set)

# frozenset is unchangable set
my_frozenset = frozenset([1, 2, 3])

# if all elements of set my_set1 is present in set my_set2 then it is a subset of the my_set1
print(my_set1.issubset(my_set2))

# if my_set1 contains all the elements of the set my_set2 then it is called as my_set1 is the superset of my_set2
print(my_set1.issuperset(my_set2))

# if my_set1 and my_set2 have no common elements then the both sets are disjoint sets
print(my_set1.isdisjoint(my_set2))

# del is a keyword used to delete a set 
del my_set3
print(my_set3)

# checking if items exist in the set or not 
if "light" in my_set2:
    print("light is present")
else:
    print("light is absent")


