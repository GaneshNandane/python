# extracting names from the list which contains the letter "o" in the names lists using the list comprehension

names=["Milo", "Searah", "Bruno", "Anastasia", "Rosa"]
namesWith_o=[item for item in names if "o" in item]
print(namesWith_o)
