# simple program for file handling using shutil module

import shutil

# Copy a file from the source path to the destination path
shutil.copy("src_txt", "dst_txt")

# Copy an entire directory and all its contents to the destination directory
shutil.copytree("src_dir", "dst_dir")

# Move a file from the demo directory to the current directory
shutil.move("demo/sam_txt", "sam_txt")

# Delete the demo directory and all of its contents
shutil.rmtree("demo")
