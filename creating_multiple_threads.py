import threading

# Function that each thread will execute
def thread_task(task):
    # Simulate some work
    print("Task processed:", task)

# Main program starts here
if __name__ == '__main__':

    # List of tasks
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Empty list to store thread objects
    threads = []

    # Create one thread for each task
    for task in tasks:

        # Create a new thread
        thread = threading.Thread(
            target=thread_task,   # Function to execute
            args=(task,)          # Arguments passed to the function
        )

        # Store the thread in the list
        threads.append(thread)

        # Start the thread
        thread.start()

    # Wait until every thread finishes
    for thread in threads:
        thread.join()

    print("All threads have finished.")
