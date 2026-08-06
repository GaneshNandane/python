import logging

# Configure logging to display INFO level messages
logging.basicConfig(level=logging.INFO)

# Decorator that logs function calls and return values
def log_function_call(func):

    # Wrapper function that accepts any number of arguments
    def decorated(*args, **kwargs):

        # Log the function name and its arguments
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")

        # Call the original function
        result = func(*args, **kwargs)

        # Log the return value
        logging.info(f"{func.__name__} returned {result}")

        # Return the original function's result
        return result

    return decorated

# Apply the logging decorator
@log_function_call
def my_function(a, b):
    return a + b

# Call the decorated function
my_function(1, 3)
