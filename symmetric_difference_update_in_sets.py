# Simple program to demonstrate the use of symmetric_difference_update() method

# Define the first set of cities
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

# Define the second set of cities
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# Update the first set with elements that are present in either set,
# but not present in both sets
cities.symmetric_difference_update(cities2)

# Print the updated set
print(cities)
