import re

# Define a regular expression pattern to find lowercase words ending with "at"
pattern = r"[a-z]+at"

# Define the text in which we want to search for the pattern
text = "The cat is in the hat."

# Find all occurrences of the pattern in the text
matches = re.findall(pattern, text)

# Print the list of all matching words
print(matches)

# Output: ['cat', 'hat']

# Replace every word matching the pattern with "dog"
new_text = re.sub(pattern, "dog", text)

# Print the modified text
print(new_text)

# Output: "The dog is in the dog."
