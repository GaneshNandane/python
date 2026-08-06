# Take a number as input from the user
n = int(input("Enter a number: "))

# Check if the number is divisible by any number from 2 to n-1
for i in range(2, n):

    # If the remainder is 0, the number is divisible by i Therefore, it is not a prime number
    if (n % i) == 0:
        print(f"{n} is not a prime number")
        break  # Exit the loop since we have found a divisor

# The else block executes only if the loop completes without encountering a break statement
else:
    print(f"{n} is a prime number")
