# Print the iteration number using a for loop and demonstrate the else block.

for x in range(5):
    # Print the current iteration number.
    print(f"Iteration no {x + 1} in for loop")
else:
    # This block executes because the loop completed without a break.
    print("else block in loop")

# This statement executes after the loop and its else block.
print("out of loop")
