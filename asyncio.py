# asyncio
# asyncio is Python's library for asynchronous programming. It allows a program to work on other tasks while waiting for slow I/O operations
# such as network requests, database queries, or file operations. Multiple asynchronous tasks can make progress concurrently using an event loop.

# Here is an example from game development.
# While the player is playing the game, the game is simultaneously
# loading the player's inventory and quest data from a server.
# This prevents the game from freezing while waiting for data.

import asyncio

async def load_inventory():
    print("Loading inventory from the server...")
    await asyncio.sleep(3)  # Simulates a network delay
    print("Inventory loaded!")

async def load_quests():
    print("Loading quests from the server...")
    await asyncio.sleep(2)  # Simulates a network delay
    print("Quests loaded!")

async def game_loop():
    for i in range(5):
        print(f"Player is exploring... ({i + 1})")
        await asyncio.sleep(1)  # Simulates game activity

async def main():
    await asyncio.gather(
        load_inventory(),
        load_quests(),
        game_loop()
    )

asyncio.run(main())
