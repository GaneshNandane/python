# it returns the common elements of the both sets in the first set it does not return the new set it modifyes the current set  

cities={"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2={"Tokyo", "Seoul", "kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)
