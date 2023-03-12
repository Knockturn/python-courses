# https://www.youtube.com/watch?v=rfscVS0vtbw&t=6006s

is_male = True
is_tall = True

if is_male:
    print("You are a male")
else:
    print("You are a female")

if is_male & is_tall: # & is the same as 'and'
    print("You are a tall male!")
elif is_male & ~is_tall: # ~ is the same as 'not'
    print("You are a short male!")

if is_male | is_tall: # or is the same as 'or'
    print("You are a male, or tall, or both!")
else:
    print("You are neither male nor tall!")

