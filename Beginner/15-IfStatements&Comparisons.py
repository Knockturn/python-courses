# https://www.youtube.com/watch?v=rfscVS0vtbw&t=6847s

def max_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: # > might be better than >=
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(f"Function max: {max_number(3, 4, 5)}")

print(f"Built in max: {max(3, 4, 5)}") # built-in function tat does the same thing

# <= is the same as 'less than or equal to'
# >= is the same as 'greater than or equal to'
# == is the same as 'equal to'
# != is the same as 'not equal to'
