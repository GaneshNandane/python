import os

# Open the file in write-only mode.
# Create it if it does not exist.
f = os.open("Myfile.txt", os.O_WRONLY | os.O_CREAT)

# Write bytes to the file
os.write(f, b"Hello, world!")

# Close the file
os.close(f)
