# importing the lru_cache from functools module as well as importing time 
from functools import lru_cache
import time

# defining lru_cache decorator with maxsize to None 
@lru_cache(maxsize=None)

# defining the function to return multiple of 5 
def fx(n):
    
     # Simulate a slow operation by waiting for 5 seconds
    time.sleep(5)

    # returning the result 
    return n*5

# calculating for 20
print(fx(20))
print("done for 20")

# calculating for 2
print(fx(2))
print("done for 2")

# calculating for 6
print(fx(6))
print("done for 6")
