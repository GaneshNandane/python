# Simple program to generate a multiplication table and handle invalid user input using exception handling

# Try to take an integer input from the user
try:
    a = int(input("Enter the number: "))

    # Print a heading showing the multiplication table for the number entered by the user
    print(f"Multiplication table of {a} is:")

    # Generate and print the multiplication table from 1 to 10
    for i in range(1, 11):
        print(f"{a} x {i} = {a * i}")

# Handle the ValueError if the user enters a value that cannot be converted into an integer
except ValueError:
    print("Invalid Input!")

# Print a message when the program finishes
print("End of program")
