from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1) # Added to see the threads running in parallel when inspecting the Activity Monitor

threads = []
num_threads = 10


# Create threads
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# Start: Execute threads
for t in threads:
    t.start()

# Join: Wait for threads to finish (blocking the main thread, until all threads are finished)
for t in threads:
    t.join()

print('end main')