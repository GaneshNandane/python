# simple program to write contents to the file 

# Open the file in write mode
f = open('myfile.txt', 'w')

# Create a list containing multiple lines of text
# \n is used to move the text to a new line
lines = ['line 1\n', 'line 2\n', 'line 3\n']

# Write all the lines from the list into the file
f.writelines(lines)

# Close the file after writing
f.close()
