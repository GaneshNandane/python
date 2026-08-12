# Program to read and display the marks of multiple students from a file

# Open the file in read-only mode
f = open('myfile.txt', 'r')

# Each line in the file represents one student's marks
# The marks are stored in this format: Maths,English,SST
# Example: 40,35,45

# Initialize the student counter
i = 0

# Read and process each student's marks one line at a time
while True:

    # Read one student's marks from the file
    line = f.readline()

    # Stop the loop when there are no more lines to read
    if not line:
        break

    # Increase the student number by 1
    i = i + 1

    # Split the line at commas and convert each mark from a string to an integer
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])

    # Display the Maths marks after multiplying them by 2
    print(f"Marks of student {i} in Maths is: {m1 * 2}")

    # Display the English marks after multiplying them by 2
    print(f"Marks of student {i} in English is: {m2 * 2}")

    # Display the SST marks after multiplying them by 2
    print(f"Marks of student {i} in SST is: {m3 * 2}")

# Close the file after processing all the students
f.close()

