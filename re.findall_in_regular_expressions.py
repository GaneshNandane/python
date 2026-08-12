import re
pattern = r"expression"
text = "The Cat is in the hat."
matches = re.findall(pattern, text)
print(matches)
#Output:['cat', 'hat']