# using enumerate function to keep track of the index of the element with iterable in a formated way 

fruits=['apple', 'banana', 'mango']
for index,fruit in enumerate(fruits):
    # printing the index followed by the value with formated way 
    print(f'{index+1}: {fruit}')
