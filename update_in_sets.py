# Simple program to demonstrate the use of the update() method

# Define the first set of cities
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

# Define the second set of cities
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# Update the first set by adding the elements of the second set
# Duplicate elements are automatically ignored
cities.update(cities2)

# Print the updated first set
print(cities)
