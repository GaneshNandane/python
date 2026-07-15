# writing contents inside a file using write() function using for loop 

# opening a file in 'w' mode so that we can write content inside this file 
f=open('myfile.txt','w')
# initializing a list contents some elements 
lines=['line 1', 'line 2', 'line 3']
# iterating over that list and writing the list contents inside the myfile.txt file one by one with \n new line escape sequnce character
for line in lines:
    f.write(line+ '\n')
f.close()
