import os

# Execute the "dir" command and open its output as a file-like object.
f = os.popen("dir")

# Read the output produced by the "dir" command and store it in the variable 'output'.
output = f.read()

# Print the output of the command. This displays the directory listing as a string.
print(output)

# Close the file-like object after reading its contents.
f.close()
