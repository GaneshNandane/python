# Simple program to read the file contents and print them to the console

# Opening the file in read-only mode to prevent accidentally modifying or overwriting its contents
f = open('poem.py', 'r')

# Reading the file contents using the read() function and storing them in the contents variable
contents = f.read()

# Printing the contents of the file
print(contents)

# Closing the file
f.close()
