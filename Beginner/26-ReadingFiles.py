# https://www.youtube.com/watch?v=rfscVS0vtbw&t=11561s

# Reading Files

# "r" - Read - Default value, so can be omitted. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value, so can be omitted. Text mode
# "b" - Binary - Binary mode (e.g. images)
# "r+" - Read and Write - Opens a file for reading and writing, error if the file does not exist
# "a+" - Append and Read - Opens a file for appending and reading, creates the file if it does not exist
# "w+" - Write and Read - Opens a file for writing and reading, creates the file if it does not exist
# "x+" - Create and Read - Creates the specified file and opens it for reading, returns an error if the file exists
# "t+" - Text and Read - Opens a file for reading and writing in text mode, error if the file does not exist
# "b+" - Binary and Read - Opens a file for reading and writing in binary mode, error if the file does not exist
# Above can be combined with "t" for text mode and "b" for binary mode


# Open a file
myFile = open("assets/employees.txt", "r")
print(myFile.readable()) # Returns true if the file is readable
#print(myFile.read()) # Reads the entire file
#print(myFile.readline()) # Reads the first line of the file
#print(myFile.readline()) # Reads the second line of the file
#print(myFile.readlines()) # Reads the entire file and returns a list of lines
#print(myFile.readlines()[1]) # Reads the second line of the file
# The above will pop from the read file. If you want to read the file again, you will need to reopen it
myFile.close()

# Better way to open a file
with open("assets/employees.txt", "r") as myFile:
    print(myFile.readable())
    print(myFile.read())
    # The file will be closed automatically