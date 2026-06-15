# multiprocessing
# it allows you to run multiple processes in parallel to utilize the maximum performance out of the system 
# here is an example of multiprocessing where multiple processes generate world chunks with simultaniously with game loop using queues

from multiprocessing import Process, Queue
import time
import random

world_chunks = {}

def generate_chunks(chunk_id, queue):
    print(f"[Chunk {chunk_id}] Generation Started!")
    time.sleep(random.randint(2, 5))
    terrain = {
        "chunk_id": chunk_id,
        "height_map": [random.randint(0, 100) for _ in range(10)],
        "trees": random.randint(10, 50),
        "enemies": random.randint(1, 10)
    }
    queue.put(terrain)
    print(f"[Chunk {chunk_id}] Generated Successfully!")
if __name__ == "__main__":
    chunk_queue = Queue()
    active_processes = []
    player_position = 0
    print("Game Started!")
    for frame in range(20):
        print(f"\nFrame {frame}")
        player_position += 1
        print(f"Player Position: {player_position}")
        if player_position % 5 == 0:
            chunk_id = player_position // 5
            process = Process(
                target=generate_chunks,
                args=(chunk_id, chunk_queue)
            )
            process.start()
            active_processes.append(process)
            print(f"Requested Generation Of Chunk {chunk_id}")
        while not chunk_queue.empty():
            chunk_data = chunk_queue.get()
            world_chunks[chunk_data["chunk_id"]] = chunk_data
            print(
                f"Chunk {chunk_data['chunk_id']} loaded into world!"
            )
        print(f"Loaded Chunks: {list(world_chunks.keys())}")
        time.sleep(1)
    for process in active_processes:
        process.join()
    print("\nFinal World Data!")
    for chunk_id, data in world_chunks.items():
        print(
            f"Chunk {chunk_id} | "
            f"Trees: {data['trees']} | "
            f"Enemies: {data['enemies']}"
        )
    print("\nGame Closed!")
