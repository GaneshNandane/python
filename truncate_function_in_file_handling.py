# Simple program to demonstrate the use of the truncate() method

# Open the file in write mode
# If the file does not exist, it will be created
with open('sample.txt', 'w') as f:

    # Write text into the file
    f.write('Hello world!')

    # Truncate the file to 5 characters
    # All content after the first 5 characters is removed
    f.truncate(5)

# Open the file in read mode
with open('sample.txt', 'r') as f:

    # Read and print the contents of the file
    print(f.read())
