import threading
def my_func():
    print("Hello from thread", threading.current_thread().name)
    thread.start()
    thread.join()