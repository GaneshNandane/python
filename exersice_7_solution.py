# changing file names in numbered order 

# importing os to work with files and folders
import os

# providing folder name 
folder = "ClutteredFolder"

# tracking all filee present inside that folder
files = os.listdir(folder)

# adding the base value for the first file
i = 1

# iterating over a folder and tracking each file 
for file in files:
    
    # converting each file to lowercase which has .png at last 
    if file.lower().endswith(".png"):
    
        # file seperator and file rename for each folder file 
        old_name = os.path.join(folder, file)
        new_name = os.path.join(folder, f"{i}.png")

        # calling the rename to add all files into that folder 
        os.rename(old_name, new_name)

        # printing after every file rename
        print(f"Renamed: {file} -> {i}.png")

        # addint the counter for each iteration 
        i += 1
