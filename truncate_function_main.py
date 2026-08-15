# simple program to demonstrate the truncate function in file handling

# Open the file in write mode to write any content to the file.
with open('sample.txt', 'w') as f:

    # Write the given text to the file
    f.write('Hello world3!')

    # Truncate the file to the first 3 characters so it cut the file size to the 3 index 
    f.truncate(3)

# Open the file in read-only mode so prevent accident writing in the file
with open('sample.txt', 'r') as f:

    # Read and print the contents of the file
    print(f.read())
