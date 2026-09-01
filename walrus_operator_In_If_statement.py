# Simple program to demonstrate the use of the walrus operator (:=)

# Define a list of names
names = ["john", "jane", "jim"]

# Take input from the user and assign it to 'name'
# using the walrus operator (:=) while also checking
# whether the entered name is present in the list
if (name := input("Enter a name:")) in names:

    # Print a greeting if the name is found in the list
    print(f"Hello, {name}!")

# Execute this block if the name is not found
else:
    print("Name not found.")
