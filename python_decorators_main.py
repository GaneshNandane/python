# Defining a decorator function
def greet(fx):

    # Defining a wrapper function to add extra functionality
    def mfx(*args, **kwargs):

        # Printing a message before calling the original function
        print("Good Morning")

        # Calling the original function with its arguments
        fx(*args, **kwargs)

        # Printing a message after calling the original function
        print("Thanks for using this function")

    # Returning the wrapper function
    return mfx

# Applying the greet decorator to the hello function
@greet
def hello():
    print("Hello World")

# Applying the greet decorator to the add function
@greet
def add(a, b):
    print(a + b)

# Calling the decorated hello function
hello()

# Calling the decorated add function with two arguments
add(1, 2)
