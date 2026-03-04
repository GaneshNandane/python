# dictionary is the ordered data of key value pairs which do not allow duplicate keys because it override the previous data present in that key
# dictionary syntax
            # dictionary_name = {"key1":'value1', "key2":'value2', "key3":'value3', ........}
# dictinary is defined as the dictionary name followed by the assiagnment operator and curly braces insede it each value is seperated by quoma and each value has two parts the first one is key and the second one is value seperated by : 

phone_directory = {"Suresh":'9027380428', "Kaushal":'9945443335', "Adesh":'9320389045', "Swapnil":'8320256915'}
print(phone_directory)
print(phone_directory.keys())
print(phone_directory.values())


for key in phone_directory.keys():
  print(f"The value coresponding to the key {key} is {phone_directory[key]}")

print(phone_directory.items())
for key, value in phone_directory.items():
  print(f"The corresponding to the key {key} is {value}")
