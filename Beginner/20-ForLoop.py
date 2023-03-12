# https://www.youtube.com/watch?v=rfscVS0vtbw&t=9164s

friends = ["Joey", "Chandler", "Monica", "Ross", "Rachel", "Phoebe"]

for friend in friends: # for each friend in the list friends.
    print(friend)

for index in range(10): # range(stop)
    print(f"index {index}")

for index in range(3, 10): # range(start, stop)
    print(f"index {index}")

for index in range(len(friends)): # len() returns the length of the list.
    print(f"index-len {friends[index]}") # prints the index of the list.

for index in range(5): 
    if index == 0: 
        print("First iteration")
    else:
        print("Not first")