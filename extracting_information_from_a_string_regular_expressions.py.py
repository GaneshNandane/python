# Importing the regular expression (re) module
import re

# String containing an email address
text = "The email address is example@example.com."

# Regular expression pattern to match an email address
# \w+  -> Matches one or more letters, digits, or underscores
# @    -> Matches the '@' symbol
# \.   -> Matches a literal dot (.)
pattern = r"\w+@\w+\.\w+"

# Searching the text for the first occurrence of the email pattern
match = re.search(pattern, text)

# Checking if an email address was found
if match:
    # Extracting the matched email address
    email = match.group()

    # Printing the extracted email address
    print(email)
else:
    # Printing a message if no email address is found
    print("No email address found.")
