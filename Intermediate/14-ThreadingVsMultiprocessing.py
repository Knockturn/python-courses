# Threading and Multiprocessing in Python
''' 
THEORY:
A process is an instance of a program in execution.
Starting a process takes a lot of resources.
Great for CPU intensive tasks.


A thread is a subset of a process.
A process can have multiple threads.
Starting a thread is much faster than starting a process.
Great for I/O intensive tasks.

GIL ( Global Interpreter Lock )
Python has a GIL (Global Interpreter Lock) that allows only one thread to execute at a time.
This is a problem for CPU intensive tasks.
How to solve this problem?
- Use Multiprocessing instead of Threading
- Use C extensions (Cython, CFFI, Numba, etc.)
- Numpy and Scipy are written in C and are python wrappers around C code.
'''