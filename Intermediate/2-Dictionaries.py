# Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

# Accessing items
value = mydict["name"] # get the value of the key "name"
print(value)

# Adding items
mydict["email"] = "max@xyz.com" # add a new key-value pair
print(mydict)

# Removing items
del mydict["email"] # remove the key-value pair with the key "name"
print(mydict)
mydict.pop("city") # remove the key-value pair with the key "name"
print(mydict)

# Check if key exists
if "name" in mydict:
    print(mydict["name"])

# Looping
for key in mydict:
    print(key)
for value in mydict.values():
    print(value)
for key, value in mydict.items():
    print(key, value)

# Copying
mydict3 = mydict.copy() # copy the dictionary to a new. Simply setting mydict3 = mydict will then reference the same dictionary.

# Merging
mergeDict1 = {"name": "Max", "age": 28, "email": "mail@xyz.com"}
mergeDict2 = dict(name="Mary", age=27, city="Boston")
mergeDict1.update(mergeDict2) # merge the two dictionaries. If there are duplicate keys, the values from mergeDict2 will be used.
print(mergeDict1)

# using tuples as keys (only immutable types can be used as keys!)
mytuple = (8, 7)
mySumDict = {mytuple: 15}
print(mySumDict)