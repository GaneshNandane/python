# lists are the data type in python which can store multiple values inside one variable 
# here values can be strings and numbers
# syntax to define a valid list
        # list_name = [value_one, value_two, value_three, ..........]
# list can be define by a list name followed by the assignment operator and squared brackets with each value seperated by quoma 

# example of the valid list
list_of_places = ["Darjiling", "Varanasi", "Omkareshwar", "Leh", "Spiti Vally", 4, 3, 2, 1]

# prof of that the above list is a valid list using the type fuction which can show us the type of a variable
print(type(list_of_places))

# printing the above list
print(list_of_places)

# here in the list we can access each element by an indexing here we have two types of indexing one is positive and another is negative indexing

# positive indexing 
print(list_of_places[0])
print(list_of_places[1])
print(list_of_places[2])
print(list_of_places[3])
print(list_of_places[4])
print(list_of_places[5])
print(list_of_places[6])
print(list_of_places[7])
print(list_of_places[8])

# here we can not access the value if the index is greater than the length of the list it gives us and out of index error
print(list_of_places[9]) # this give us error showing out of index

# negative indexing
print(len(list_of_places))
print(list_of_places[-1])
print(list_of_places[-2])
print(list_of_places[-3])
print(list_of_places[-4])
print(list_of_places[-5])
print(list_of_places[-6])
print(list_of_places[-7])
print(list_of_places[-8])

# we can know more about list using if else statement that if we want to know if a value in a list is present or not 
# here we are accessing a value which are present in a list that are a number
if 4 in list_of_places:
  print("yes")
else:
  print("No")

# we can know more about list using if else statement that if we want to know if a value in a list is present or not 
# here we are accessing a value which are present in the list that are a string 
if "Omkareshwar" in list_of_places:
  print("yes")
else:
  print("No")

# we can show a list in a perticluar range also by using indexing similar to above we just need to add one more : and spacify the end of the list 
print(list_of_places[0:4])

# we can show a list in a perticluar range also by using indexing similar to above we just need to add one more : and spacify the end of the list 
# here we add another : and it is used for a jump index by providing this we just jump to the that index 
print(list_of_places[0:9:2])

# iterating throughout a list
for i in list_of_places:
  print(i)

