# # In python there are two types of typecasting are present
#             |
#             |
#             | -----> Implicit typecasting 
#             |        In implicit typecasting pyton automatically convert one data tyoe to another operation 
#             |
#             |------> Explicit typecasting
#             |        In Explicit typecasting programmer specify what data type it need to use 

# typecasting for int 
memory_address1 = 4
print(type(memory_address1))

# typecasting for float
memory_address2 = 4.5
print(type(memory_address2))

# There are two conditions occur here including a letter and a number
# typecasting for string number
memory_address3 = "4"
print(type(memory_address3))

# typecasting for string letter
memory_address4 = "g"
print(type(memory_address4))


# IMPLICIT TYPECASTING


n = memory_address1 + memory_address2
print(n)
print(type(n))

n = memory_address1 * memory_address2
print(n)
print(type(n))
          

# EXPLICIT TYPECASTING


# convert float to int 
n = int(memory_address2)

print(n)
print(type(n))
          
# here is a exception for converting string to the int or float data type there must be a valid numnber like "5" and not any letter like "n" becase python does not know that n is any number 
# condition 1
# convert string to int for number  
n = int(memory_address3)

print(n)
print(type(n))

# condition 2
# convert string to int for letter
# this below code gives error because the value of memory_address4 is letter and letters cannot be added to intiger without typecasting 
# n = int(memory_address4)

# print(n)
# print(type(n))

# this gives error because there is different data types
# n = memory_address1 + memory_address4
# print(n)        
# print(type(n))

# this is valid because we typecast it
n = memory_address1 + int(memory_address3)
print(n)        
print(type(n))

# convert int to float
n = float(memory_address1)

print(n)
print(type(n))

# convert string to float
n = float(memory_address3)

print(n)
print(type(n))

# convert int to string
n = str(memory_address1)

print(n)
print(type(n))

# convert float to string 
n = str(memory_address2)

print(n)
print(type(n))


