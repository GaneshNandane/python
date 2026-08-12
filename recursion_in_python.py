# Define a function to calculate the factorial of a number using recursion
def factorial(num):

    # Return 1 when the number is 0 or 1 because 0! and 1! are both equal to 1
    if num == 1 or num == 0:
        return 1

    # Multiply the current number by the factorial of the previous number
    # The function keeps calling itself until it reaches 1 or 0
    else:
        return num * factorial(num - 1)

# Driver code to test the factorial function
num = 7

# Display the number whose factorial is being calculated
print("Number:", num)

# Calculate and display the factorial of the given number
print("Factorial:", factorial(num))
