# tuple operations 
# tuples are immutable in python so we need to convert it into list to perform operations on it 

# defining a tuple 
countries=("Spain", "Italy", "India", "England", "Germany")

# converting tuple into list 
temp=list(countries)

# adding element into list 
temp.append("Russia")   #add item

# converting the list into tuple 
countries=tuple(temp)

# printing the tuple 
print(countries)

# converting tuple into list 
temp=list(countries)

# removing an element from the list
temp.pop(3)     #remove item

# converting the list into tuple 
countries=tuple(temp)

# printing the tuple 
print(countries)

# converting tuple into list 
temp=list(countries)

# changing the element of the index 3 
temp[2]="Finland"   #change item

# converting the list into tuple 
countries=tuple(temp)

# printing the tuple 
print(countries)
