# list methods are used to manipulate lists

# these are two lists that are used as an example to the below methods
list_of_fruit_names = ["Guava", "Banana", "Apple", "Watermelon", "Grapes", "Pineapple", "mango", "Apple"]
list_of_fruit_names2 = ["Custeredapple", "kiwi"]

# printing both lists
print(list_of_fruit_names)
print(list_of_fruit_names2)

# append method adds and element to the end
list_of_fruit_names.append("Papaya")
print(list_of_fruit_names)

# pop deletes the element at an specified index
list_of_fruit_names.pop(0)
print(list_of_fruit_names)

# sort sorts the value in and ascending and descending order
list_of_fruit_names.sort(reverse=True)
print(list_of_fruit_names)

# reverse is used to reverse the list
list_of_fruit_names.reverse()
print(list_of_fruit_names)

# index used to show the index of an specified element
print(list_of_fruit_names.index("Banana"))

# count counts the number of element occurence inside list
print(list_of_fruit_names.count("Apple"))

# extend is used to add element from other list to the existing list
list_of_fruit_names.extend(list_of_fruit_names2)
print(list_of_fruit_names)

# insert inserts an element at a specified index
list_of_fruit_names.insert(3, "Orange")
print(list_of_fruit_names)

# copy copyes whole list and prints new list with similar values inside it
print(list_of_fruit_names.copy())
