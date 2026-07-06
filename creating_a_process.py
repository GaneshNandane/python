import multiprocessing
def my_function():
    print("Hello from process", multiprocessing.current_process().name)
    process = multiprocessing.process(target = my_function)
    process.start()
    process.join()