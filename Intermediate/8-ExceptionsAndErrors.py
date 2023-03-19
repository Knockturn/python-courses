# Errors and Exceptions
# Try and use specific errors instead of general ones. 

# Syntax Errors
# a = 5 print (a) # SyntaxError: invalid syntax

# Exceptions
#a = 5 + '10' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# try and except
try:
    a = 5 + '10'
except:
    print('There was an error')

# try, except, else
try:
    a = 5 + 10
except:
    print('There was an error')
else:
    print('There was no error')

# try, except, else, finally
try:
    a = 5 + 10
except:
    print('There was an error')
else:
    print('There was no error')
finally:
    print('This code will always run')

# Raising an Exception
try:
    a = 5 + '10'
except:
    print('There was an error')
    #raise # This will raise the error again

# Raising a specific Exception
try:
    a = 5 + '10'
except TypeError:
    print('There was a type error')

# Define your own Exception
class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)