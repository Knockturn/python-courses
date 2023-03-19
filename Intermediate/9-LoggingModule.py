# The logging module is a standard library module that provides a simple interface to the logging system in Python.

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
import helper
helper.logger.debug('This is a debug message via the imported helper module')
