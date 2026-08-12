# simple program to read the file contents and print that on to the console

# opening a file in read only mode so that no one unintatially override any content into the file which might be not good
f=open('poem.py', 'r')

# reading the file contents using read function and sotring the file content into the contents variable 
contents=f.read()

# printing the contents variable
print(contents)
