# to find double space in the following string
name = "Hi how are you my i help you"
print(name.find("  "))

# after adding double space it gives the index of the double space
name = "Hi how are  you my i help you"
print(name.find("  "))

# Note: if it does not find it then it return -1 
# Note: it finds first occurence of the match in the parent string
