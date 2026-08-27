# Simple program to demonstrate the use of the symmetric_difference() method

# Define the first set of cities
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

# Define the second set of cities
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# Find the cities that are present in either set but not in both sets
# The result is stored in a new set called cities3
cities3 = cities.symmetric_difference(cities2)

# Print the resulting set
print(cities3)
