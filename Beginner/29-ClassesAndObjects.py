# https://www.youtube.com/watch?v=rfscVS0vtbw&t=13436s

# Classes are used to create new user-defined data structures that contain arbitrary information about something.
# An object is an instance of a class. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.
from assets.student import Student # See .\assets\student.py

student = Student("Jim", 23, "Business", 3.1, False) # This is how you create an object from a class
student2 = Student("Pam", 54, "Art", 3.8, False) # If you are missing a parameter, you will get an error on runtime
print(student.name)
print(student2.gpa)