'''
Process
A Process is an instance of a program, e.g. a Python interpreter. They are independent from each other and do not share the same memory.

Key facts: - A new process is started independently from the first process - 
Takes advantage of multiple CPUs and cores - Separate memory space - Memory is not shared between processes 
- One GIL (Global interpreter lock) for each process, i.e. avoids GIL limitation 
- Great for CPU-bound processing - Child processes are interruptable/killable

Starting a process is slower that starting a thread
Larger memory footprint
IPC (inter-process communication) is more complicated

Threads
A thread is an entity within a process that can be scheduled for execution (Also known as "leightweight process"). A Process can spawn multiple threads. The main difference is that all threads within a process share the same memory.

Key facts: - Multiple threads can be spawned within one process - Memory is shared between all threads - Starting a thread is faster than starting a process - Great for I/O-bound tasks - Leightweight - low memory footprint

One GIL for all threads, i.e. threads are limited by GIL
Multithreading has no effect for CPU-bound tasks due to the GIL
Not interruptible/killable -> be careful with memory leaks
increased potential for race conditions
'''

# Threads in python
"""
Despite the GIL it is useful for I/O-bound tasks when your program has to talk to slow devices, like a hard drive or a network connection.
With threading the program can use the time waiting for these devices and intelligently do other tasks in the meantime.

Example: Download website information from multiple sites. Use a thread for each site.
"""
# Note: The following example usually won't benefit from multiple threads since it is CPU-bound. It should just show the example of how to use threads.

from threading import Thread

def square_numbers():
    for i in range(1000):
        result = i * i


if __name__ == "__main__":        
    threads = []
    num_threads = 10

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()

# Multiprocessing in python
"""
It is useful for CPU-bound tasks that have to do a lot of CPU operations for a large amount of data and require a lot of computation time. 
With multiprocessing you can split the data into equal parts an do parallel computing on different CPUs.

Example: Calculate the square numbers for all numbers from 1 to 1000000.
Divide the numbers into equal sized parts and use a process for each subset.
"""
from multiprocessing import Process
import os


def square_numbers():
    for i in range(1000):
        result = i * i


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main thread until these processes are finished
    for process in processes:
        process.join()