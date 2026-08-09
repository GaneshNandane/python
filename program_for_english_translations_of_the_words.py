# simple program to know the english meaning of the hindi words using a dictionary

# defining a dictionary
words = {
    "madat":"Help",
    "billi":"Cat",
    "kursi":"Chair"
}

# accessing the user input and matching it to the key value pairs
word = input("Enter the word you want meaning of:")

# printing the value to the respective key
print(words[word])
 
