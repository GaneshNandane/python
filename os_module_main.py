# Import the os module to work with files and directories
import os

# Check if a folder named "data" already exists. If it does not exist, create it.
if (not os.path.exists("data")):
    os.mkdir("data")

# Create 100 subfolders inside the "data" directory. The folders will be named:
# day1, day2, day3, ..., day100
for i in range(0, 100):
    os.mkdir(f"data/day{i+1}")
