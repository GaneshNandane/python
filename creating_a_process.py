import multiprocessing

# Function that will be executed by the child process
def my_function():
    print("Hello from process:", multiprocessing.current_process().name)


# This ensures the code below runs only when this file is executed directly
if __name__ == "__main__":

    # Create a new child process
    process = multiprocessing.Process(target=my_function)

    # Start the child process
    process.start()

    # Wait for the child process to finish
    process.join()

    print("Main process finished.")
