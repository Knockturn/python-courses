# The logging module is a standard library module that provides a simple interface to the logging system in Python.
# Notice rotating file handler at the bottom.

import logging
# The logging module has 5 levels of logging:
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# By default, the logging module will only log messages with a level of WARNING or higher.
# to change this, we can use the basicConfig() method to set the level of logging.
logging.basicConfig(level=logging.DEBUG) # set directly after importing the module

# You can format the logging messages by passing a format string to the basicConfig() method.
# Example: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# datefmt='%m/%d/%Y %I:%M:%S %p' can be used to format the date/time.

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Best practice is to use the logging module in a module, and then import the logger into other modules.
# This way, you can control the logging level in one place, and all the modules will use the same logging level.
# Example:
print('\n Importing the helper module...')
import helper # See Intermediate/helper.py
helper.logger.debug('This is a debug message via the imported helper module')
# See helper.py for writing to a file.
helper.logger.error('This is an error message will be written to a file', exc_info=True) # exc_info=True will log the exception info.

# logging.conf
# The logging module can be configured using a configuration file.
from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
# Above line gets the path to the current file, and then appends 'logging.conf' to the end of it.
# Without it we would have to use an absolute path, which would not work on other computers.
import logging.config
logging.config.fileConfig(log_file_path)
logger2 = logging.getLogger('simpleExample')
logger2.debug('This is a debug message')

# Rotating File Handler
# The RotatingFileHandler class is used to create a file handler that will rotate the log file when it reaches a certain size.
# Example:
from logging.handlers import RotatingFileHandler
logger3 = logging.getLogger('RotatingFileHandler')
logger3.setLevel(logging.INFO)
# Create a handler that will rotate the log file when it reaches 2KB.
# The backupCount argument specifies how many backup files to keep.
handler = RotatingFileHandler('rotating.log', maxBytes=2000, backupCount=5)
logger3.addHandler(handler)
for i in range(10000):
    logger3.info('This is line %s' % i)

# Timed Rotating File Handler
# The TimedRotatingFileHandler class is used to create a file handler that will rotate the log file at certain timed intervals.
# Example:
from logging.handlers import TimedRotatingFileHandler
import time
logger4 = logging.getLogger('TimedRotatingFileHandler')
logger4.setLevel(logging.INFO)
# Create a handler that will rotate the log file every minute.
handler = TimedRotatingFileHandler('timed.log', when='s', interval=2, backupCount=5)
logger4.addHandler(handler)
for i in range(3):
    logger4.info('This is line %s' % i)
    time.sleep(2)

# Python json logger is a library that allows you to log in JSON format.