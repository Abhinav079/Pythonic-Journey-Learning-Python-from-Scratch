#Multithreading is a technique where multiple threads are used to execute multiple tasks concurrently within a single process

import threading
import time

def task1():
    for i in range(5):
        print("Task 1 - iteration:", i)
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2 - iteration:", i)
        time.sleep(2)

# create two threads for two tasks
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# start the threads
thread1.start()
thread2.start()

# wait for the threads to finish
thread1.join()
thread2.join()

print("All tasks completed.")
