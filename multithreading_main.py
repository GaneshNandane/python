# Import the threading module to create and manage threads
import threading

# Import the time module for sleep() and measuring execution time
import time

# Import ThreadPoolExecutor for managing a pool of worker threads
from concurrent.futures import ThreadPoolExecutor

# Function that simulates a task by sleeping for a given number of seconds
def func(seconds):

    # Display how long the thread will sleep
    print(f"Sleeping for {seconds} Seconds")

    # Pause the current thread for the specified number of seconds
    time.sleep(seconds)

    # Return the sleep duration after the task is completed
    return seconds

# Function demonstrating multithreading using the threading module
def main():

    # Record the starting time of the program
    time1 = time.perf_counter()

    # Create three thread objects
    # target = function to execute
    # args = arguments passed to the function
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    # Start all three threads
    # They begin executing simultaneously
    t1.start()
    t2.start()
    t3.start()

    # Wait until all threads have completed their execution
    t1.join()
    t2.join()
    t3.join()

    # Record the ending time
    time2 = time.perf_counter()

    # Print the total execution time
    print("Total time with threading:", time2 - time1)

# Function demonstrating ThreadPoolExecutor
def poolingDemo():

    # Create a thread pool
    # Python automatically creates and manages worker threads
    with ThreadPoolExecutor() as executor:

        # Submit individual tasks to the thread pool
        # submit() immediately returns a Future object
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 2)
        future3 = executor.submit(func, 4)

        # result() waits until the corresponding task is completed
        # and then returns its return value
        print(future1.result())
        print(future2.result())
        print(future3.result())

        # List of sleep durations
        l = [3, 5, 1, 2]

        # map() applies func() to every element of the list
        # The tasks are executed concurrently
        results = executor.map(func, l)

        # Print the return value of every completed task
        for result in results:
            print("Result from map:", result)

# Execute the threading example
main()

# Execute the ThreadPoolExecutor example
poolingDemo()
