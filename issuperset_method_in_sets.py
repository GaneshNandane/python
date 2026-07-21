# The issuperset() method checks whether the first set contains all the elements of the second set. It returns True if all the elements of the second set are present in the first set; otherwise, it returns False. 

# defining two sets 
cities={"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2={"Seoul", "Kabul"}

# checking if the cities is a superset of cities2 
print(cities.issuperset(cities2))

# defining a new set 
cities3={"Tokyo", "Madrid", "Delhi"}

# checking if the cities is a superset of cities3 
print(cities.issuperset(cities3))
