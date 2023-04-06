# Multiprocessing is a technique where multiple processes are used to execute multiple tasks concurrently.
# Unlike multithreading, multiprocessing allows tasks to run in separate memory spaces, 
# which can help avoid issues such as race conditions and deadlocks that can occur in multithreaded programs.

if __name__ == '__main__':
    import multiprocessing

    num_cpus = multiprocessing.cpu_count()
    print("Number of CPUs:", num_cpus)

    from multiprocessing import cpu_count
    import time

    def task1():
        for i in range(5):
            print("Task 1 - iteration:", i)
            time.sleep(1)

    def task2():
        for i in range(5):
            print("Task 2 - iteration:", i)
            time.sleep(1)

# create two processes for two tasks
    process1 = multiprocessing.Process(target=task1)
    process2 = multiprocessing.Process(target=task2)

# start the processes
    process1.start()
    process2.start()

# wait for the processes to finish
    process1.join()
    process2.join()

    print("All tasks completed.")
