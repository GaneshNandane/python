# importing the different library's for using the asyncronous functions
# here in this program there are three different functions that are async menas that all the three functions must return it's value to the main function always  

import time
import asyncio
import requests

# function1 is the function that goes to the url provided in this program using the requests.get() method and downloads that files to the instagram.ico file if file is not present then python automatically creates one 
async def function1():
    print("func 1")
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
    
    return "Harry"
    
# function2 is the function that goes to the url provided in this program using the requests.get() method and downloads that files to the instagram2.jpg file if file is not present then python automatically creates one 
async def  function2():
    print("func 2")
    URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram2.jpg","wb").write(response.content)
    
# function3 is the function that goes to the url provided in this program using the requests.get() method and downloads that files to the instagram3.ico file if file is not present then python automatically creates one 
async def function3():
    print("func 3")
    URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    response = requests.get(URL)  
    open("instagram3.ico", "wb").write(response.content)

# this function binds all the async functions into a giant wrapper to call all the async functions all functions must reaturn any value if not program might fail 
async def main():
  # await function1()
  # await function2()
  # await function3()
  # return 3
  L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
  print(L)
  # task = asyncio.create_task(function1())
  # # await function1()
  # await function2()
  # await function3()

# this line of code starts the async event loop 
asyncio.run(main())
