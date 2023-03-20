# NOTE: Currently not working. Will throw runetime error.

from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1) # Added to see the processes running in parallel when inspecting the Activity Monitor

processes = []
num_processes = os.cpu_count()


# Create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# Start: Execute processes
for p in processes:
    p.start()

# Join: Wait for processes to finish (blocking the main thread, until all processes are finished)
for p in processes:

    p.join()

print('end main')