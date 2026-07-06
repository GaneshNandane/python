# Import the Pool class from the multiprocessing module Pool is used to create a group of worker processes that can execute tasks in parallel.
from multiprocessing import Pool


# Function that will be executed by the worker processes Each worker receives one task from the tasks list.
def process_task(task):
    # Simulate processing the given task Here we simply print the task number.
    print("Task processed:", task)


# This block ensures that the code inside it runs only when this file is executed directly. It prevents child processes from repeatedly executing the main program (especially important on Windows).
if __name__ == '__main__':

    # Create a list of tasks that need to be processed Each number represents an individual task.
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Create a pool containing 4 worker processes At most 4 tasks can be processed simultaneously.
    with Pool(processes=4) as p:

        # The map() function distributes the tasks among the worker processes.
        #
        # Internally:
        # Worker 1 -> process_task(1)
        # Worker 2 -> process_task(2)
        # Worker 3 -> process_task(3)
        # Worker 4 -> process_task(4)
        #
        # As soon as a worker finishes, it automatically picks up the next available task until all tasks are completed.
        #
        # Since process_task() does not return anything 'results' will contain a list of None values.
        results = p.map(process_task, tasks)

    # After exiting the 'with' block:
    # - All worker processes are automatically closed. The program waits until every task has finished.
