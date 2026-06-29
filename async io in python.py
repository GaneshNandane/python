import asyncio
async def my_async_function():
    #asynchronous code here 
    await asyncio.sleep(1)
    return "Hello, async world!"  
async def main():
    result = await my_async_function() 
    print(result)
asyncio.run(main())