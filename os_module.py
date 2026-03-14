# os module in python is used to interact with the operating system  we can create folders interact with the files and can runs system commands in the system 
# note: this program might not work for all the systems i program this code according to my system you can write your own according to your use 
import os


# printing the name of the current directory 
print(os.getcwd())

# printing the list of the various files that are present in the current directory 
print(os.listdir())

# it prints environment variables that system uses to interact with the softwares it is like key value pairs
print(os.environ)

# this line prints all folders files in the current directory 
os.system("dir")

# this function is used to rename the file with the specified new name in the parameters of the rename function
if os.path.exists("Text.txt"):
  os.rename("Text.txt", "text.txt")
  print("file name renamed")
else:
  print("file does not exists.")

# this function is used to create a new folder in current directory named NewFolder 
if os.path.exists("NewFolder"):
  os.rmdir("NewFolder")
  print("folder removed.")
else:
  print("folder do not exists.")
