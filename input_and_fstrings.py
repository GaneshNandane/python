# input fuction is used to extract the user inputs from the input devices to the cosole 
# input functions can be executed one by one and we can add multiple input functions in a program and they run top to bottom where top gets executed first and it waits for the user input at each function
# input function treats every input as a strig data type we need to typecast for other 
# fstrings in the python can be use to add functions variables directly in to the string

name = input("Enter your name: ")
print(f"my name is {name}")

surname = input("Enter your surname: ")
print(f"my surname is {surname}")

# example of fstrings
print(f"my name is {name} {surname}")
