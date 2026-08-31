# Simple program to demonstrate the use of the update() method in dictionaries

# Define a dictionary with key-value pairs
info = {'name': 'karan', 'age': 19, 'eligible': True}

# Print the original dictionary
print(info)

# Use the update() method to modify the value of an existing key
info.update({'age': 20})

# Use the update() method to add a new key-value pair to the dictionary
info.update({'DOB': 2001})

# Print the updated dictionary
print(info)
