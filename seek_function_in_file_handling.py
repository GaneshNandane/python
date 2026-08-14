# Simple program to read 5 characters starting from index 10 of file.txt

# Open the file in read-only mode to prevent accidentally modifying its contents
with open('file.txt', 'r') as f:

    # Move the file pointer to index 10
    f.seek(10)

    # Read the next 5 characters starting from index 10
    data = f.read(5)

    # Print the characters read from index 10 up to, but not including, index 15
    print(data)
