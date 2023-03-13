# class for 29-ClassesAndObjects.py & 31-ObjectFunction.py
class Student:
    def __init__(self, name, age, major, gpa, is_on_probation):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


    # Below created in 31-ObjectFunction.py
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False