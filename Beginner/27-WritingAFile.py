# https://www.youtube.com/watch?v=rfscVS0vtbw&t=12086s

# Appending to a file

# Better way to write to a file
with open("assets/employees.txt", "a") as my_file: # Be careful with "a" as it will append to the file
    my_file.write("\nKelly - Customer Service") # Adds a new line to the file
    my_file.write("\nToby - Human Resources") # Adds a new line to the file

'''
Jim - Salesman
Dwi - Salesman
Pam - Receptionist
Michael - Manager
'''

# Writing to a file (overwrites the file)
#with open("assets/employees.txt", "w") as file: # Be careful with "a" as it will append to the file
#    file.write("Kelly - Customer Service") # Adds a new line to the file

# Writing to a file (creates a new file, or overwrites the file if it exists)
with open("assets/index.html", "w") as file: # Be careful with "a" as it will append to the file
    file.write("<p>This is HTML</p>") # Adds a new line to the file