# https://www.youtube.com/watch?v=rfscVS0vtbw&t=15157s

from assets.chef import Chef
from assets.chineseChef import ChineseChef

myChef = Chef()
myChef.make_chicken() # prints "The chef makes chicken" from the class Chef

myChineseChef = ChineseChef()
myChineseChef.make_chicken() # prints "The chef makes chicken" from the class Chef
myChineseChef.make_fried_rice() # prints "The chinese chef makes fried rice" from the class ChineseChef
myChineseChef.make_special_dish()