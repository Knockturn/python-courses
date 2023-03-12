# https://www.youtube.com/watch?v=rfscVS0vtbw&t=11057s

# Try and Except is similar to try/catch in other languages

success = False

while not success:
    try:
        number = int(input("Enter a number: "))
        success = True
    except: # Bad practice to use except without specifying the error
        print("Invalid input, try again")

# try and except are used to catch errors in code and handle them gracefully instead of crashing the program
# Above it is also used to ensure that the user enters a valid number and not a string

# You can also be specific about the error you want to catch

success2 = False

while not success2:
    try:
        number2 = int(input("Enter a number: "))
        success2 = True
    except ValueError as err: # This will only catch ValueErrors and save the error message as err
        print("Invalid input, try again")
        print(err)