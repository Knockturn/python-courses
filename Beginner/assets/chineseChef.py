# Inheritance
# Gets all the methods and attributes from the chef class
from assets.chef import Chef
class ChineseChef(Chef):
    def make_fried_rice(self):
        print("The chinese chef makes fried rice")

    def make_special_dish(self): # Overriding the method from the chef class
        print("The chinese chef makes orange chicken")