# issubset() method checks if the elements of the first set are present in the second set 
# it returns True if they are present in the second set otherwise it returns False 

# defining two sets 
cities={"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2={"Delhi", "Madrid"}

# printing if the cities2 is the subset of cities 
print(cities2.issubset(cities))
