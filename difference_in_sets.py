# difference in sets

# we need to initialize two sets and need to perform difference() method on them 
# Note: difference does not modify the original set it returns new set 
cities={"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2={"Seoul", "Kabul", "Delhi"}

# The difference() method returns a new set containing elements that are in the first set but not in the second set
cities3=cities.difference(cities2)

# printing the new set after performing the difference() method on it 
print(cities3)
