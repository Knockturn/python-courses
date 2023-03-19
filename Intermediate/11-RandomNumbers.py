# Random Module: Sudo random numbers
# Secrets Module: Cryptographically secure random numbers
# Numpy Random Module: Random numbers for numpy arrays
'''
Activate the virtual environment "source env_intermediate/bin/activate" in terminal
Run the file "python3 Intermediate/11-RandomNumbers.py" in terminal
'''

import random
import secrets
import numpy as np

print("Random Module")
a = random.random() # Returns a random float between 0 and 1
print(a)

b = random.randint(1, 10) # Returns a random integer between 1 and 10
print(b)

c = random.choice([1, 2, 3, 4, 5]) # Returns a random element from a list
print(c)
# random.shuffle([1, 2, 3, 4, 5]) # Shuffles a list
# random.sample([1, 2, 3, 4, 5], 3) # Returns a list of 3 random elements from a list
# seed() # Sets the seed for the random number generator
random.seed(1) # Sets the seed for the random number generator
# Above makes the random numbers predictable

#----------------------------------------#
# Cryptographically secure random numbers, used for passwords, security keys, etc.
print("Secrets Module")
d = secrets.randbelow(10) # Returns a random integer between 0 and 9
print(d)

e = secrets.randbits(4) # Returns a random integer between 0 and 15
print(e)

f = secrets.choice([1, 2, 3, 4, 5]) # Returns a random element from a list
print(f)

#----------------------------------------#
# Random numbers for numpy arrays, used for machine learning
print("Numpy Random Module")
g = np.random.rand(3, 3) # Returns a 3x3 array of random floats between 0 and 1
print(g)
