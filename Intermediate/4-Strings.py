# Ordered, immutable, text representation
'''
Single or double quotes are fine.
Triple quotes are used for multi-line strings.
Escape characters are used to represent special characters. ´\n´ is a new line.
You can concatenate strings with +.
You can multiply strings with *.
You can use the in operator to check if a string is in another string.
f-strings are used to format strings. They are prefixed with f and can contain expressions inside curly braces.
'''
# Character of string
my_string = "Hello World"
char = my_string[0] # H
print(char)
# Slicing
slice = my_string[0:5] # Hello
print(slice)

# String methods
# len() returns the length of a string
# lower() returns the string in lower case
# upper() returns the string in upper case
# strip() removes any whitespace from the beginning or the end
# replace() replaces a string with another string
# split() splits the string into substrings if it finds instances of the separator
# count() returns the number of times a specified value occurs in a string
# find() searches the string for a specified value and returns the position of where it was found
# format() formats specified values in a string
# capitalize() converts the first character to upper case
# casefold() converts string into lower case
# center() returns a centered string
# encode() returns an encoded version of the string
# endswith() returns true if the string ends with the specified value
# expandtabs() sets the tab size of the string
# isalnum() returns True if all characters in the string are alphanumeric
# isalpha() returns True if all characters in the string are in the alphabet
# isdecimal() returns True if all characters in the string are decimals
# isdigit() returns True if all characters in the string are digits
# isidentifier() returns True if the string is an identifier
# islower() returns True if all characters in the string are lower case
# isnumeric() returns True if all characters in the string are numeric
# isprintable() returns True if all characters in the string are printable
# isspace() returns True if all characters in the string are whitespaces
# etc... https://www.w3schools.com/python/python_ref_string.asp