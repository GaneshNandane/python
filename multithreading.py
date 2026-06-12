# multithreading

# multithreading is a technique where multiple threads execute concurrently within the same process
# a thread is a lightweight unit of execution within a process
# multiple threads can run concurrently to perform tasks simultaneously
# here is an example of multithreading in a multiplayer game
# here we run two threads: the main game loop and a network thread that receives enemy data

import threading
import time
import random

enemy_positions = []

def recive_enemy_data():
    while True:
        time.sleep(3)
        
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        
        enemy_positions.append((x, y))
        
        print(f"\n [server] enemy positions ditected ({x}, {y})")

network_thread = threading.Thread(
    target = recive_enemy_data,
    daemon = True
)

network_thread.start()

for frame in range(15):
    print(f"\n[Game] Frame {frame}")
    print("[Game] player is moveing...")
    
    if enemy_positions:
        print("[Game] Visible enemies:", enemy_positions)
    time.sleep(1)
print("\n Game closed !")
