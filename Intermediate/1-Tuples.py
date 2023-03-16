# Tuple: ordered, immutable, allows duplicate elements

# TL;DR: Tuples are like lists, but they are immutable. They are faster than lists, but you can't change them.

myTuple = (5, True, "Hello", True, 5.5, 5)
alsoTuple = 5, True, "Hello", True, 5.5, 5 # you don't need the parenthesis
rememberComma = ("5",) # if you have only one item, you need a comma at the end

# unpacking
a, b, c, d, e, f = myTuple # you can unpack a tuple into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
# Remember that the order matters when unpacking, as well as the number of variables

my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple # you can unpack a tuple into variables, and use the * to group items into a list
print(i1)
print(i2)
print(i3)