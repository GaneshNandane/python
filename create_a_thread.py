# creating a thread and executing them 

# here threading works to do multiple tasks concurrently in the same program without threading task runs sequntially 
import threading
import time

# task one 
def task1():
    print("Task 1 started")
    time.sleep(3)
    print("Task 1 finished")

# task two 
def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task 2 finished")

# creating a thread one
t1 = threading.Thread(target=task1)
# creating a thread two 
t2 = threading.Thread(target=task2)

# starting both the threads simultaneously
t1.start()
t2.start()

# ending both the threads 
t1.join()
t2.join()

# printing that the both the tasks completed  
print("Both tasks completed")
