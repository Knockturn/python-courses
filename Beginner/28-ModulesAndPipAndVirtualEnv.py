# https://www.youtube.com/watch?v=rfscVS0vtbw&t=12493s

# Modules are just other python files that you can import into your project
# You can import modules from the standard library or from other people
# You can also create your own modules

# https://docs.python.org/3/py-modindex.html - Python Moduel Index, all these are built-in and doesn't need to be installed
# External modules need to be installed using pip. Ex: https://python-docx.readthedocs.io/en/latest/user/install.html#install -> pip install python-docx
# pip is a package manager for python. It allows you to install and manage external packages that are useful to your projects
# Best practice is to create a virtual environment for each project. This is a folder that contains all the dependencies for a specific project

# "python -m venv env_beginner" -> creates a virtual environment called env_beginner (windows)
# "python3 -m venv env_beginner" -> creates a virtual environment called env_beginner (macOS)

# "env_beginner\Scripts\activate" -> activates the virtual environment (windows)
# "source env_beginner/bin/activate" -> activates the virtual environment (macOS)

from assets import useful_tools # This is how you import a module from another file in a subfolder
# import useful_tools # This is how you import a module from another file in the same folder

print(f"Random dice roll: {useful_tools.roll_dice(10)}")
