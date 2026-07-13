# coding and decoding

# taking input for the coding 
st = input("Enter message")

# spliting the words for further coding an the basis of space 
words = st.split(" ")

# taking input for selecting coding or decoding 
coding = input("1 for coding or 0 for decoding")

# checking if the entered input is added for the coding or decoding and printing the output 
coding = True if (coding == "1") else False
print(coding)

# if the user entered coding then the if block is being executed if not then else block is executed 
if(coding):
    # creating an empty list to store the each text provided by the user and by spliting them in a list for the coding
    nwords = []

    # iterating over each word of the list for applying coding 
    for word in words:

        # if the length of the word is greater then we are adding the some bizare text at front and end to encode each word
        if(len(word) >= 3):
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)

        # if the length of the word is less than 3 then we simply reverse that word
        else:
            nwords.append(word[::-1])

    # joining all the encoded words into a single string separated by spaces and printing the output
    print(" ".join(nwords))

# if the user selects decoding then this block is executed
else:

    # creating an empty list to store the decoded words
    nwords = []

    # iterating over each encoded word for decoding
    for word in words:

        # checking if the encoded word length is greater than or equal to 3
        if len(word) >= 3:

            # removing the first and last three characters that were added during encoding
            stnew = word[3:-3]

            # moving the last character to the front to restore the original word
            stnew = stnew[-1] + stnew[:-1]

            # adding the decoded word into the list
            nwords.append(stnew)

        # if the word length is less than 3 then reversing it restores the original word
        else:
            nwords.append(word[::-1])

    # joining all the decoded words into a single string separated by spaces and printing the final output
    print(" ".join(nwords))
