# unordered, mutable, no duplicate elements
# set is a collection of unique elements
myset = {1, 2, 3, 4, 5, 5} # duplicate elements are ignored
print(myset)

stringSet = set("Hello") # order will be random, one l will be ignored
print(stringSet)

# add element to set
myset.add(6)
print(myset)

# remove element from set. Will throw error if element is not in set
myset.remove(3)

# discard element from set. Will NOT throw error if element is not in set
myset.discard(9)

# You can pop an element from set. It will remove a random element and return it
lastItemInSet = myset.pop()
print(lastItemInSet)
'''
'''
# Union combines two sets (ignores duplicates) and returns a new set
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
u = odds.union(evens) # union of odds and evens
print(u)
# Intersection returns a new set with elements common to both sets
i = odds.intersection(primes)
print(i) # {3, 5, 7}
# Difference returns a new set with elements in the first set but not in the second
d = odds.difference(primes)
print(d) # {1, 9}
# Symmetric Difference returns a new set with elements in either set but not both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
sd = setA.symmetric_difference(setB)
print(sd) # 1, 2, 3 are in both sets, so they are removed completely.

# update() method updates the set by adding items from another set
setA.update(setB)
print(setA) # Will add 10, 11, 12 to setA
# intersection_update() method updates the set by keeping only the elements found in it and an other set
newSetA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
newSetB = {1, 2, 3, 10, 11, 12}
newSetA.intersection_update(newSetB)
print(newSetA) # {1, 2, 3}

'''
OTHERS:
'''
# difference_update() method updates the set by removing elements found in another set
# symmetric_difference_update() method updates the set by only keeping the elements found in either set, but not in both
# isdisjoint() method returns True if two sets have a null intersection
# issubset() method returns True if another set contains this set
# issuperset() method returns True if this set contains another set
