# This program classifies a number into different categories.
# It demonstrates the use of nested if-else statements.

num = 18

# Check if the number is negative
if (num < 0):
    print("Number is negative.")

# If the number is positive, classify it based on its range
elif (num > 0):

    # Check if the number lies between 1 and 10
    if (num <= 10):
        print("Number is between 1-10.")

    # Check if the number lies between 11 and 20
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")

    # If none of the above conditions are true, the number is greater than 20
    else:
        print("Number is greater than 20")

# If the number is neither positive nor negative, it must be zero
else:
    print("Number is zero")
