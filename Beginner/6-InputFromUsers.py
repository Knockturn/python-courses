# https://youtu.be/rfscVS0vtbw?t=2906

name = input("Enter name, please: ")
age = input("Enter age, please: ")
print("Thanks " + name + "!")
if type(age) != int:
    print("That is not a number!")
else:
    print("You are " + age + " years old!")