# program to find the patterns using re module 

import re

# Defining the regular expression pattern to find words ending with "at"
pattern = r"\b\w*at\b"

# Defining the text in which we want to search for the pattern
text = "The Cat is in the hat."

# Finding all words that match the pattern
matches = re.findall(pattern, text, re.IGNORECASE)

# Printing the matched words
print(matches)

# Output: ['Cat', 'hat']
