# Because tuples are immutable there is minimum methods that are present in the python

# example of tuple
trees = ("Neem", "Babhud", "Wad", "Pipal", "Sag", "Neem", "Wad", "Pipal")

# printing the tuple
print(trees)

# count method
# count method counts the number of elements that are present in the repeated manner
print(trees.count("Neem"))

# index method tells us the index of the element
print(trees.index("Wad"))

# here is the index method that checks a element in an specific range
print(trees.index("Sag", 2, 5))

# len method is used to find length of the tuple
print("Length of the trees tuple is: ",len(trees))
