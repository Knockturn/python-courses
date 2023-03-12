# https://www.youtube.com/watch?v=rfscVS0vtbw&t=5055s

# say_hi("P", 36) # NameError: name 'say_hi' is not defined

def say_hi(name, age):
    print(f"Hello {name}, you are {age}")

print("Above the function call")
say_hi("Mike", 35)
print("Below the function call")