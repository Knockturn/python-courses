# https://www.youtube.com/watch?v=HGOBQPFzWKo&t=56s

# Lists: Ordered, Mutable, allows duplicate elements
mylist = [5, True, "Hello", True, 5.5, 5]

if "Hello" in mylist:
    print("Hello is in the list")

print(len(mylist)) # len = length

mylist.append("World") # add to the end of the list
mylist.insert(0, "First") # add to the beginning of the list because of the 0 index

item = mylist.pop() # return and remove the last item from the list
print (item)

item2 = mylist.pop(0) # return and remove the first item from the list because of the 0 index
print (item2)

mylist.remove(True) # remove the first item that matches the value
print(mylist)

#new_list = sorted(mylist) # return a new list with the sorted items. Does not change the original list. Dont mix string and int.
#print(new_list)

a = mylist[1:3] # return a new list with the items from index 1 to 3
print(a)

b = mylist[1:] # return a new list with the items from index 1 to the end
print(b)

c = mylist[:3] # return a new list with the items from index 0 to 3
print(c)

d = mylist[::2] # return a new list with the items from index 0 to the end with a step of 2
print(d)