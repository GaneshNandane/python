# docstrings are normal strings technically speaking every string that are place after the definition of the function definintion class definition or module definition we can call it a docstrings
# docstrings are used for the knowing the function working of any issues related to that function if the programmer facing any issues reagarding how this function works he can call __doc__ function to know the working  of that function or module or class we can accesss the all the containts of the docstrings by help() also

# we can disscuss the difference between the strings comments and docstrings below

# comment example
# this is the commment

# this is the string
name = "Ganesh Harichandra Nanadne"

# this is the docstrings example
def square(n):
    """
    Calculates the square of a number.

    Parameters:
        n (int or float): The number to be squared.

    Returns:
        int or float: Square of n.
    """
    return n ** 2

# this is the fuction definition where we are calculating the square root of the number 5
print(square(5))

# doc funcion prints the all docstring to be able to know how any function or module works
print(square.__doc__)

# help function prints the all docstring in the proper formated way 
help(square)
