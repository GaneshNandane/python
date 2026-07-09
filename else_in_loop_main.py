# Initialize the variable 'i' to 0.
i = 0

# The while loop will continue to execute as long as i is less than 7.
while i < 7:

    # Print the current value of i.
    print(i)

    # Increment the value of i by 1.
    i = i + 1

    # Check if i has become 4.
    if i == 4:

        # Exit the while loop immediately.
        # Since the loop is terminated using 'break',
        # the else block of the loop will NOT execute.
        break

# This else block executes only if the while loop
# finishes normally (i.e., without encountering a break).
else:
    print("sorry no i")
