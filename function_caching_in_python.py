# Importing the functools module and Applying the lru_cache decorator.with maxsize=None means there is no limit on the number of cached results.
import functools
@functools.lru_cache(maxsize=None)
def fib(n):

    # Base case:
    # If n is 0 or 1, return n directly.
    if n < 2:
        return n

    # Recursive case:
    # Fibonacci number = previous Fibonacci + second previous Fibonacci
    return fib(n - 1) + fib(n - 2)

# Calling the function to find the 20th Fibonacci number
print(fib(20))
