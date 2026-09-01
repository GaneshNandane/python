import multiprocessing

def producer(queue):
    for i in range(10):
        queue.put(i)

def consumer(queue):
    while True:
        item = queue.get()
        print(item)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    
    p1 = multiprocessing.Process(target=producer, args=(queue,))
    p2 = multiprocessing.Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
