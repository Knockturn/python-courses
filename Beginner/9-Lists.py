# https://youtu.be/rfscVS0vtbw?t=3792

# Lists are build-in data structures in Python.
# Lists are mutable, meaning the value of elements of a list can be altered.
# Arrays are not built-in in Python, but can be created using the array module.

friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']

# Lists can be indexed and sliced
print(friends[0])
print(friends[1:3]) # Up to but not including the third element

# Access list from the end
print(friends[-1]) # Last element

# Mutable example
friends[1] = 'David'
print(friends)

# Lists can be concatenated
friends = friends + ['Terry', 'Lucy']
print(friends)