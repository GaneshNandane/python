import os
#open the file in write only mode
f=os.open("Myfile.txt", os.O_WRONLY)

#write to the file
os.write(f, b"Hello, world !")

#close the file
os.close(f)