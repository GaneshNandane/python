# Program to read the contents of a file and print them to the console

# Opening the file in read-only mode
f = open('myfile.txt', 'r')

# Using an infinite loop to read the file line by line
while True:

    # Reading one line from the file
    line = f.readline()

    # Stopping the loop when there are no more lines to read
    if not line:
        break

    # Printing the current line
    print(line)

# Closing the file after reading its contents
f.close()
