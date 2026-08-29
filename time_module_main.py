# Simple program to demonstrate the use of the time module

# Import the time module
import time

# Define a function that prints numbers from 1 to 50000 using a while loop
def usingWhile():

    # Initialize the counter variable
    i = 0

    # Repeat the loop until i reaches 50000
    while i < 50000:

        # Increase the value of i by 1
        i = i + 1

        # Print the current value of i
        print(i)

# Define a function that prints numbers from 0 to 49999 using a for loop
def usingFor():

    # Use range() to generate numbers from 0 to 49999
    for i in range(50000):

        # Print the current value of i
        print(i)

# Store the current time before running the for loop
init = time.time()

# Call the function that uses the for loop
usingFor()

# Calculate and store the time taken by the for loop
t1 = time.time() - init

# Store the current time before running the while loop
init = time.time()

# Call the function that uses the while loop
usingWhile()

# Calculate and print the time taken by the while loop
print(time.time() - init)

# Print the time taken by the for loop
print(t1)

# Print the number 4
print(4)

# Pause the program for 3 seconds
time.sleep(3)

# Print this message after the 3-second delay
print("This is printed after 3 seconds")

# Get the current local date and time
t = time.localtime()

# Format the current time into Year-Month-Day Hour:Minute:Second format
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

# Print the formatted current date and time
print(formatted_time)
