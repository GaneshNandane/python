# enumerate is a python function that is used to loop over an iterable with keep track of index 

# here in this program we are looping over a list using iterable using enumerate with index of 1 
fruits=['apple', 'banana', 'mango']
for index,fruit in enumerate(fruits, start=1):
    # printing all values of the list using for loop with enumerate function to keep track over index from 1 
    print(index, fruit)
