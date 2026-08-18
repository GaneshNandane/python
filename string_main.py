# Simple program to demonstrate strings, string indexing, and string iteration

# Define a string containing a person's name
name = "Harry"

# Define strings containing the names of a friend and another friend
friend = "Rohan"
anotherfriend = "Lovish"

# Define a multiline string using triple single quotes
apple = '''He said,
Hi Harry
Hey I am good
"I want to eat an apple"'''

# Concatenate two strings and print the greeting
print("Hello, " + name)

# Print the complete multiline string
print(apple)

# Access and print individual characters of the string using indexing
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# Print a message before starting the for loop
print("Let's use a for loop\n")

# Iterate through each character of the apple string
for character in apple:

    # Print each character one at a time
    print(character)
