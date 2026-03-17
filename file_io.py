# file input output is the important in the python because of python works with various files 
# note: file system is a wide topic to talk about and has much more in the advance to study all about 
# there are mainlly four functions that works with the files system they are 
            # 1. open()
              # open method is used to open a file that is being already there or already created 
            # 2. read()
              # read method is used to read the existing containts of the file that are present in the file 
            # 3. write()
              # write method is used to write containts inside the existing file
            # 4. close()
              # close method is used to close the file that is been updated by writing contiants to that file 

# note: make sure to close your file after every change in the file 

# example of reading a file which is already existed 
file = open('Text.txt', 'r')
data = file.read()
print(data)
file.close()

# reading file line by line
file = open('Text.txt', 'r')
print(file.readline())
print(file.readline())
file.close()

# reading file in line by line in one go 
file = open('Text.txt', 'r')
print(file.readlines())
file.close()

# example of writing to a file which is already existed 
file = open('Text.txt', 'w')
file.write("Hello how are you ?")
file.close()

# example of writing to a file in append mode so that containts of the file should not override 
file = open('Text.txt', 'a')
file.write("We are good friends now ?")
file.close()

# safe way to reading and writing files using with keyword so that we do not have to use the close method everytime
with open('Text.txt', 'r') as file:
  print(file.read())
