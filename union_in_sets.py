# Simple program to demonstrate the use of the union() method

# Define the first set of cities
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

# Define the second set of cities
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# Use the union() method to combine both sets
# Duplicate values are automatically removed
# The result is stored in a new set
cities3 = cities.union(cities2)

# Print the new set containing all unique cities
print(cities3)
