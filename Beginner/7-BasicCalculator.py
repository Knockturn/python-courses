print("This program adds two numbers whole numbers")
print("Will round if you enter a decimal number")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = round(float(num1)) + round(float(num2))
print(type(result))
if type(result) != int:
    print("That is not a number!")
else:
    print(f"The sum is {result}")