# program to write contents to the file 

# opening the file in the write mode to write any contents to the file 
# Note: in write mode the file contents can be overriden
f=open('myfile.txt','w')

# contents that is going to write into the file
lines=['line 1\n', 'line 2\n', 'line 3\n']

# adding contents to the file 
f.writelines(lines)

# closeing the file
f.close()
