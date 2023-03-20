# Generators are functions that return an object (iterator) which we can iterate over (one value at a time).
# More memoery efficient than lists. Used in machine learning a lot.
def my_generator():
    yield 1
    yield 2
    yield 3

# Once the item has been yielded, it is removed from the generator.

g = my_generator()
print(next(g)) # next is a built in function that returns the next value in the generator
print(next(g))

h = my_generator()
for i in h:
    print(i)

i = my_generator()

print(sum(i))

#.sorted() is a built in function that sorts a list. It returns a new list, it does not change the original list.

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(5)

value = next(cd)
print(value)
# It will remember the state and continue from there. So will continue loop from 4.
print(next(cd))

# Memory efficient
# In a large dataset, you don't want to store all the values in memory. You want to generate them as you need them.
# In a normal function, you would have to store all the values in memory.
print("\nMemory efficient")
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn_generator(10))
print(sum_of_first_n)