# extractging the names from the list if the length of the names is greater than 4 using list comprehension

names=["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
long_name=[item for item in names if (len(item)>4)]
print(long_name)
