# lambda arguments : expression
# Best practice: Use lambda functions when an anonymous function is required for a short period of time.
# lambda functions are used along with built-in functions like filter(), map() etc.
# If you need to do the action multiple times, then you can use a normal function instead of a lambda function.

# Example 1
# Add 10 to argument a, and return the result:
print("Example 1")
add10 = lambda x : x + 10
print(add10(5))
# Normal function Version:
def add_10(x):
    return x + 10
print(add_10(5))

# Example 2
# Multiply argument a with argument b and return the result:
print("Example 2")
mult = lambda x, y : x * y
print(mult(5, 6))
# Normal function Version:
def multiply(x, y):
    return x * y
print(multiply(5, 6))

# Example 3
# Sort
print("Example 3")
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
print(points2D_sorted) # sorted by x, if x's are equal then sorted by y
points2D_sorted = sorted(points2D, key=lambda x: x[1]) # sort by y value
print(points2D_sorted)

# Example 4
# Filter will return an iterator that contains only the values that return True when passed into the function.
print("Example 4")
a = [1, 2, 3, 5, 7, 10, 13]
a = list(filter(lambda x: x % 2 == 0, a))
print(a)
# List Comprehension Version (easier to read):
a = [1, 2, 3, 5, 7, 10, 13]
a = [x for x in a if x % 2 == 0]
print(a)

# Example 5
# Map will return an iterator that contains the results of the function applied to each item of the iterable.
print("Example 5")
a = [1, 2, 3, 5, 7, 10, 13]
a = list(map(lambda x: x * 2, a))
print(a)
# List Comprehension Version (easier to read):
a = [1, 2, 3, 5, 7, 10, 13]
a = [x * 2 for x in a]
print(a)

# Example 6
# Reduce will return a single value that is the result of the function applied to the first two items of the iterable,
# then that result is applied to the function with the third item, and so on.
print("Example 6")
from functools import reduce
a = [1, 2, 3, 5, 7, 10, 13]
a = reduce(lambda x, y: x + y, a)
print(a)
# List Comprehension Version (easier to read):
a = [1, 2, 3, 5, 7, 10, 13]
a = sum(a)
print(a)