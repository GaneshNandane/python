# strings are the data type in python that stores the sequnce of characters in a variable there are two ways that string can be defined
    # 1. in double quotaion marks
          # "  "
    # 2. in single quotation marks
          # '  '
    # 3. in triple double quotation marks
          # """  """
    # 4. in triple single quotation marks
          # '''  '''

# Example using double qotation makrs
name = "Ganesh"

# Example using single quoatation marks
surname = 'Nandane'

# Example using triple double quotation makrs
message = """Hello everyone i am Ganesh Nandane, i am an undergraduate student of Artificial Intelligence and Data Science. My message to everyone is stay happy at your pace"""

# Example using triple single quotation marks
sumarry = '''All people have different pace of learning in their academic carrier'''

print(f"Hello, {name} {surname}")

# accessing element from the variable string data type include two ways 
      # 1. by print statement
      # 2. by for loop statement

# we can access each of the element of the string characters one by one through print statement with the variable name followed by the square brackets and give the number called as the index of the character in the variable name

# indexing works as the leftmost element is 0 and the as you go towards the right side of the variable name the value gets increase considering one example we can understand indexing
                                  # G  a  n  e  s  h
                                  # |  |  |  |  |  |   
                                  # 0  1  2  3  4  5
          
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# we can also access each of the element of the string characters one by one through for loop by looping the variable name
for characters in surname:
  print(characters)
