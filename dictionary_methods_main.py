# dictonary and it's methods 

# initializing two dictonaries 
ep1={122:45, 123:89, 567:69, 670:69}
ep2={222:67, 566:90}

# updating the first dictionary to add new contents of the second dictionary into first dictionary using update() method 
ep1.update(ep2)
print(ep1)

# deleting a certain provided key value pairs from the dictionary using the pop() keyword 
ep1.pop(122)
print(ep1)

# deleting the key value pairs from the dictionary which is at last index using popitem() method 
ep1.popitem()
print(ep1)

# deleting a certain provided key value pair in the dictionary using del keyword
del ep1[123]
print(ep1)

# clearing the containts of the dictionary using the clear() method 
ep1.clear()
print(ep1)

