# https://www.youtube.com/watch?v=rfscVS0vtbw&t=14908s

from assets.student import Student # See .\assets\student.py

student1 = Student("Jim", 23, "Business", 3.1, False)
student2 = Student("Pam", 54, "Art", 3.8, False)

print(f"Student1 is on honor roll: {student1.on_honor_roll()}") # This is how you call a function from a class
print (f"Student2 is on honor roll: {student2.on_honor_roll()}")