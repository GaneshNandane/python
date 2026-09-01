# Simple program to demonstrate multiprocessing using a Queue for communication between processes

# Import the multiprocessing module
import multiprocessing

# Define a producer function to add values to the queue
def producer(queue):

    # Generate numbers from 0 to 9
    for i in range(10):

        # Add each generated value to the queue
        queue.put(i)

# Define a consumer function to get values from the queue
def consumer(queue):

    # Continuously check for values in the queue
    while True:

        # Get the next value from the queue
        item = queue.get()

        # Print the value received from the queue
        print(item)

# Run the following code only when the program is executed directly
if __name__ == '__main__':

    # Create a multiprocessing queue for communication
    # between the producer and consumer processes
    queue = multiprocessing.Queue()

    # Create a process for the producer function
    p1 = multiprocessing.Process(
        target=producer,
        args=(queue,)
    )

    # Create a process for the consumer function
    p2 = multiprocessing.Process(
        target=consumer,
        args=(queue,)
    )

    # Start the producer process
    p1.start()

    # Start the consumer process
    p2.start()

    # Wait for the producer process to finish
    p1.join()
