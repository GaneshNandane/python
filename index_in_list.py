# Example of using the index() method with a list of colors

# Creating a list of colors
colors = ["Voilet", "Green", "Indigo", "Blue", "Green"]

# Finding the index (position) of the first occurrence of "Green"
# Although "Green" appears twice, index() returns only the first occurrence.
print(colors.index("Green"))

# Example of using the index() method with a list of numbers

# Creating a list of numbers
num = [4, 2, 5, 3, 6, 1, 2, 1, 3, 2, 8, 9, 7]

# Finding the index (position) of the first occurrence of the number 3
# The number 3 appears at index 3 and index 8, but index() returns the first one.
print(num.index(3))
