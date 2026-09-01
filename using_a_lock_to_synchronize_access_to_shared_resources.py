# Simple program to demonstrate multithreading and the use of a lock

# Import the threading module
import threading

# Define a function to increment the shared counter
def increment(counter, lock):

    # Repeat the increment operation 10,000 times
    for i in range(10000):

        # Acquire the lock so only one thread can access
        # the shared counter at a time
        lock.acquire()

        # Increment the shared counter by 1
        counter[0] += 1

        # Release the lock so another thread can access the counter
        lock.release()

# Run the following code only when this file is executed directly
if __name__ == '__main__':

    # Store the counter inside a list so both threads
    # can modify the same counter
    counter = [0]

    # Create a lock to synchronize access to the shared counter
    lock = threading.Lock()

    # Create an empty list to store the thread objects
    threads = []

    # Create and start two threads
    for i in range(2):

        # Create a thread that will execute the increment() function
        thread = threading.Thread(
            target=increment,
            args=(counter, lock)
        )

        # Add the thread object to the threads list
        threads.append(thread)

        # Start the thread
        thread.start()

    # Wait for all threads to finish their execution
    for thread in threads:
        thread.join()

    # Print the final value of the shared counter
    print("Counter value:", counter[0])
