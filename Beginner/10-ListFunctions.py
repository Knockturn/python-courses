# https://www.youtube.com/watch?v=rfscVS0vtbw&t=4244s

lucky_numbers = [42, 8, 15, 16, 23, 2]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

friends.sort() # Sort the list
print(friends)

friends.extend(lucky_numbers) # Add the list to the end of the list. Note: Now sort will not work as the list has both strings and numbers
print(friends)

friends.append("Creed") # Add to the end of the list
print(friends)

friends.insert(1, "Kelly") # Add to the list at a specific index
print(friends)

friends.remove("Jim") # Remove the first instance of the value
print(friends)

friends.pop() # Remove the last item in the list
print(friends)

print(friends.index("Jim")) # Find the index of the value. # ValueError: 'Jim' is not in list if not found
print(friends.count("Jim")) # Count the number of times the value appears in the list

lucky_numbers.reverse()
print(f"Reverse: {lucky_numbers}") # Reverse the list

friends2 = friends.copy() # Copy the list
print(f"Copy: {friends2}")

friends.clear() # Clear the list
print(friends)