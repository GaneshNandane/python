# program to find the pattern on the basis of if the pattern is avaiable then printing match found else match not found 

import re

# Define a regular expression pattern
pattern = r"world"

# Define the text in which we want to search for the pattern
text = "Hello world!"

# Search for the pattern in the text
match = re.search(pattern, text)

# Check whether a match was found
if match:
    print("Match found!")
else:
    print("Match not found.")
