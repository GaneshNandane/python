# WRITING A File

# writing a file in the mode 'a' (append) mode so that the file content can not get overide and if the file does not exist then it is being created on the go 
with open('file_for_manipulating_files.py', 'a')as f:
    f.write("Hey i am inside this file")
    
# READING A File
# reading a file in the 'r' (reading) mode so we can only read the file content and not make changes accidently 
f=open('file_for_manipulating_files.py', 'r')
file = f.read()

# printing file content 
print(file)

# close the file after reading 
f.close()
