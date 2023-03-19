# Serialize and deserialize JSON
# https://youtu.be/HGOBQPFzWKo?t=9740
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# dumping to file
with open('Intermediate/person.json', 'w') as file:
    json.dump(person, file, indent=4)

# Parse JSON into a dictionary (deserialize or decode)
person = json.loads(personJSON)
print(person)

# loading from file
with open('Intermediate/person.json', 'r') as file:
    person = json.load(file)
    print(person)


# From class to JSON
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

use = User('John', 30)
userJSON = json.dumps(use.__dict__)
print(userJSON)
