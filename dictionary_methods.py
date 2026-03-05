# this is the example of the dictonary with different the dictionary methods

phone_directory = {"Suresh":'9027380428', "Kaushal":'9945443335', "Adesh":'9320389045', "Swapnil":'8320256915'}
print(phone_directory)

# get method is used to extract the specific value correspnding to the key specified by the user
print(phone_directory.get("Kaushal"))

# update method is used to update the dictonary values correspinding to the key specified by the user
phone_directory.update({"Kaushal":'9403940210'})
print(phone_directory)

# copy is used to create a new dictionary similar to the one that we are copying
new_directory = phone_directory.copy()
print(new_directory)

# pop is used to delete a spcified key value pair in the dictionary 
phone_directory.pop("Suresh")
print(phone_directory)

# popitem is used to delete the last key value pair that are present in the last of the dictionary
phone_directory.popitem()
print(phone_directory)

# clear is used to clear all the key value pairs that are present inside the dictionary
phone_directory.clear()
print(phone_directory)

# fromkeys are used to create a dictionary by using any python build in data types and all the value corresponding to the all keys are same that the user provide
check_list = {"Backpack", "Grapling Hook", "Water Bottle", "Rope"}
check = dict.fromkeys(check_list, "checked")
print(check)

# del is used to delete a spacified kay value pairs in the dictionary
del check["Grapling Hook"]
print(check)
