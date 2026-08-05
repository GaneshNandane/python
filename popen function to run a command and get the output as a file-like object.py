import os
#Run the "ls" command and get the output as a file-like object
f=os.popen("ls")

#Read the contents of the output
output=f.read()
print(output)       #output:['myfile.txt', 'otherfile.txt']

#close the file-like object
f.close()