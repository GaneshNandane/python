import os

# Open the file in read-only mode
f = os.open("Myfile.txt", os.O_RDONLY)

# Read up to 1024 bytes from the file
contents = os.read(f, 1024)

# Convert bytes to a string and print the contents
print(contents.decode())

# Close the file
os.close(f)
