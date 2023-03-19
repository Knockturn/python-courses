# Collections Module: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
print("Counter")
a = "aaaaabbbbbbcccccc"
my_counter = Counter(a) # Counts the number of each letter in the string. Key Value pair
print(my_counter)
print(my_counter.most_common(1)) # Returns the most common letter as a list of tuples
print(my_counter.most_common(2)) # Returns the 2 most common letters
print(my_counter.most_common(1)[0]) # Returns the most common letter as a tuple because it is the first element in the list
print(my_counter.most_common(1)[0][0]) # Returns the most common letter as a string because it is the first element in the tuple
# my_counter.elements() # Returns an iterator that returns each element in the counter

# namedtuple, created a class with attributes
print("Named Tuple")
Point = namedtuple('Point', 'x,y') # Creates a class called Point with x and y attributes. Comma or space separated
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# OrderedDict, keeps the order of the keys. In python 3.7+ dictionaries are ordered by default
print("Ordered Dict")
ordered_dict = OrderedDict()
ordered_dict['a'] = 1 # Adds a key value pair
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict) # Prints the dictionary in the order the keys were added

# defaultdict, sets a default value for a key if it doesn't exist
print("Default Dict")
d = defaultdict(int) # Sets the default value to 0
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['b'])
print(d['c']) # Returns 0 because it doesn't exist

# deque, double ended queue. Add and remove from both ends
print("Deque")
d = deque()
d.append(1) # Adds to the right
d.append(2)
d.appendleft(3) # Adds to the left
print(d)