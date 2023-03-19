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


#----------------------------------------#
print("Secrets Module")
d = secrets.randbelow(10) # Returns a random integer between 0 and 9
print(d)

e = secrets.randbits(4) # Returns a random integer between 0 and 15
print(e)

f = secrets.choice([1, 2, 3, 4, 5]) # Returns a random element from a list
print(f)

#----------------------------------------#
print("Numpy Random Module")
g = np.random.randint(1, 10) # Returns a random integer between 1 and 9
print(g)
