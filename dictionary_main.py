# dictionary 

# initializing a dictionary 
info={'name':'karan', 'age':19, 'eligible':True}

# printing the dictionary 
print(info)

# printing all the keys that are present inside the dictionay 
print(info.keys())

# printing all the values that are present inside the dictionary 
print(info.values())

# iterating over key values and printing the key value pairs corresponding to each other 
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")
    
# printing the key value pairs as an single items in the dictionary 
print(info.items())

# iterating over items inside the dictionary to print the key corresponding to the value 
for key,value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
