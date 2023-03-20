# Decorators are used to modify the functionality of a function without changing the code of the function itself.
# Two kinds of decorators: Function decorators and Class decorators
# Function Decorators are mostly used when you want to add some functionality to an existing function.
# Class Decorators are used mostly when you want to change or update the state of an object.
# You can stack decorators on top of each other.

# Function Decorators
import functools

def start_end_decorator(func):
    @functools.wraps(func) # This is used to preserve the name of the function
    def wrapper(*args, **kwargs): # *args and **kwargs are used to pass any number of arguments to the function
        print("Start: Do something before the function is called")
        result = func(*args, **kwargs)
        print("End: Do something after the function is called")
        return result # This is used to return the result of the function
    return wrapper

@start_end_decorator
def add_5(x):
    return x + 5

print(add_5(10))

# Decorators with Arguments
print("\n")
print("Decorators with Arguments")
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("John")

# Stacking Decorators:
@repeat(num_times=5)
@start_end_decorator
def say_hello():
    print("Hello")
say_hello()
'''
----------------
----------------
'''
# Class Decorators
print("\nClass Decorators")

class CountCalls:
    def __init__(self, func): # This is used to initialize the class
        self.func = func # This is used to store the function
        self.num_calls = 0

    def __call__(self, *args, **kwargs): # This is used to call the function
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@repeat(num_times=3)
@CountCalls
def say_my_name():
    print("Hello, my name is John")

say_my_name()