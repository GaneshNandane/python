# command line utility 
    # command line utility or (CLI) are the program that runs on the user commands and arguments on to the terminal or command prompt 

# texture assets organizer 

# here is an example of the texture and assets organizer in a game development workflow before importing into the game engine we need to handle the resources of the game in formated way 
import argparse
import os

# here is the argument parser object 
parser = argparse.ArgumentParser(
    description="Game Texture Asset Organizer"
)

# creating command line argument named folder
parser.add_argument(
    "folder",
     help = "folder containing texture files"    
)

# reading command line arguments specified by the user
args = parser.parse_args()

# checks if the folder exist or not if not then program terminates automatically through exit(1)
if not os.path.isdir(args.folder):
    print(f"\n Error: folder {args.folder} not found")
    print("please check the path and try again.")
    exit(1)
    
# only valid texture formats
texture_formats = [".png", ".jpg", ".jpeg"]

# displaying scaned information with the seperator
print(f"\nScaning folder:  ", {args.folder})
print("-" * 100)

# Counter to keep track of the number of texture files processed
total_files = 0

# returns all files inside the folder
# like this
        # textures/
            # |
            # | ground.png
            # | grass.jpg
            # | tree.jpeg
                
for filename in os.listdir(args.folder):
# Create the complete file path
    file_path = os.path.join(args.folder, filename)
# checking if it is file or not file and spliting file with their name and extension 
    if os.path.isfile(file_path):
        name, extension = os.path.splitext(filename)
# Convert the extension to lowercase and check whether it is a supported texture format
        if extension.lower() in texture_formats:
            total_files += 1
            new_name = (name.lower().replace(" ", "_") + extension.lower())
            new_path = (os.path.join(args.folder, new_name))
            os.rename(file_path, new_path)
            print(f"processed: {filename}")
            print(f"Renamed to: {new_name}\n")
# printing total number of files that are present inside the folder
print(f"-" * 100)
print("total texture files processed ", total_files)
