# extracting the file names that are present inside the current dirctory 

import os
#Get a list of the files in the current directory
files=os.listdir(".")
print(files)        #output:{'myfile.txt', 'otherfile.txt'}
