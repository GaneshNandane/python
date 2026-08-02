import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Simulated task
def func(seconds):
    print(f"Sleeping for {seconds} Seconds")
    time.sleep(seconds)
    return seconds

def main():
    time1 = time.perf_counter()

    # Creating and starting threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])
    
    t1.start()
    t2.start()
    t3.start()

    # Wait for threads to finish
    t1.join()
    t2.join()
    t3.join()

    time2 = time.perf_counter()
    print("Total time with threading:", time2 - time1)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # Submitting tasks individually
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 2)
        future3 = executor.submit(func, 4)

        print(future1.result())
        print(future2.result())
        print(future3.result())

        # Submitting multiple tasks with map
        l = [3, 5, 1, 2]  # Proper list
        results = executor.map(func, l)
        for result in results:
            print("Result from map:", result)

# Call functions
main()
poolingDemo()
