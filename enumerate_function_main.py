# Using a manual counter and the enumerate() function to produce the same output.

# Defining a list of marks
marks = [12, 56, 32, 98, 12, 45, 1, 4]


# ---------------------- Code Block 1 ----------------------

# Initializing a counter variable to keep track of the current index
index = 0

# Iterating over the list of marks
for mark in marks:
    # Printing the current mark
    print(mark)

    # Checking whether the current index is equal to 3
    if index == 3:
        print("Harry, awesome!")

    # Incrementing the index after each iteration
    index += 1


# ---------------------- Code Block 2 ----------------------

# Iterating over the list using enumerate(), which automatically provides both the index and the corresponding element. The 'start=1' argument makes indexing begin from 1 instead of 0.
for index, mark in enumerate(marks, start=1):
    # Printing the current mark
    print(mark)

    # Checking whether the current index is equal to 3
    if index == 3:
        print("Harry, awesome!")
