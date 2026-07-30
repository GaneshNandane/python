
# creating a list 
l=[11, 42, 1, 2, 4, 5, 1, 1]

# printing the list 
print(l)

# adding 7 to the last of the list 
l.append(7)

# sorting the list in decending order 
l.sort(reverse=True)

# sorting the list in assending order 
l.reverse()

# printing the index of first occurrence of 1   
print(l.index(1))

# printing how many times 1 occures in the list 
print(l.count(1))

# creating the copy of the list 
m=l.copy()

# changing the first element at index 0 in the new copied list 
m[0]=0

# inserting the element at index 2 in the list 
l.insert(4, 2)

# reassiging the list m to completelly new list 
m=[900, 1000, 1100]

# addingt the old list the the new reassigined list 
k=l+m

# printing the new list that is formed by the addition of two lists 
print(k)

# adding all elements of the list to the end of the l list 
l.extend(m)

# printing the new l list 
print(l)
