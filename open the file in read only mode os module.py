import os
#open the file in read only mode
f=os.open ("Myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)
# close the file
os.close()