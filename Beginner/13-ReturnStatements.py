# https://www.youtube.com/watch?v=rfscVS0vtbw&t=5651s

def cube(num:int): # cube is power of 3 (3*3*3. 3^3)
    result = num*num*num # result is a local variable
    return result # return statement. Return exits the function

print(cube(3)) # 27

my_result = cube(4) # 64. Store the result in a variable
print(my_result)