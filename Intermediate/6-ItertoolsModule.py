# Itertools Module, product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat

# When printing an iterable you need to convert it to a list in order to see it good.
# Otherwise it will print the memory location of the iterable

# product, returns the cartesian product of the two lists
# Useful for finding all possible combinations of two lists
print("Product")
a = [1, 2]
b = [3, 4]
prod = product(a, b, repeat=2) # repeat=2 repeats the list 2 times
print(list(prod))

# permutations, returns all possible permutations of the list
# Useful for finding all possible permutations of a list
print("Permutations")
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
perm2 = permutations(a, 2) # 2 is the length of the permutations
print(list(perm2))

# combinations, returns all possible combinations of the list
# Useful for finding all possible combinations of a list
print("Combinations")
a = [1, 2, 3, 4]
comb = combinations(a, 2) # 2 is the length of the combinations
print(list(comb))

# accumulate, returns the accumulated sum of the list
# Useful for finding the accumulated sum of a list
# Default is sum, but you can use other functions like min, max, etc.
print("Accumulate")
a = [1, 2, 3, 4]
acc = accumulate(a) # takes index value and adds it to the next index value
print(list(acc))
import operator
acc2 = accumulate(a, func=operator.mul) # takes index value and multiplies it to the next index value
print(list(acc2))

# groupby, returns the groups of the list
# Returns the groups of the list based on the key function you pass in.
print("Groupby")
def smaller_than_3(x):
    return x < 3
a = [1, 2, 3, 4]
group_by = groupby( a, key=smaller_than_3) # key=smaller_than_3 is the function that returns the key for the group
for key, value in group_by:
    print(key, list(value)) # Prints the key and the values in the group
# Grouped by the key function smaller_than_3. So 1,2 are grouped true and 3,4 are grouped false
# In future use Lambda functions for key functions
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
group_by2 = groupby(b, key=lambda x: x < 3)
for key, value in group_by2:
    print(key, list(value))

# Another clearer example below:
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
group_by3 = groupby(persons, key=lambda x: x['age'])
for key, value in group_by3:
    print(key, list(value))

# Infinite iterators
# count, returns an infinite iterator that counts up

print("Count")
for i in count(10): # 10 is the starting value
    print(i)
    if i == 15: 
        break # Breaks the loop when i is 15 otherwise it will be an infinite loop

# cycle, returns an infinite iterator that cycles through the list
print("Cycle")
a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i == 3:
        break

# repeat, returns an infinite iterator that repeats the value
print("Repeat")
for i in repeat(1, 4): # 4 is the number of times it repeats
    print(i)
