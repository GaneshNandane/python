# importing asyncio module to write and run asyncronous code it is used to handle the time bound codes that need a waiting for each function output to process it easyly without any bug 

import asyncio

# creating an asycronous function 
async def my_async_function():
    # pausing the function for one second without blocking the program   
    await asyncio.sleep(1)
    return "Hello, async world!"  

# defining the main asyncronous function 
async def main():
    result = await my_async_function() 
    print(result)
    
# returning the main asyncronous function using the asyncio event loop 
asyncio.run(main())
