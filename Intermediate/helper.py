import logging

logger = logging.getLogger(__name__)

# You can stop propagation of log messages by setting the propagate attribute to False.
# This will stop the log messages from being passed to the parent logger.
# This is useful if you want to create a logger that only logs messages from a specific module.
# Example:
# logger.propagate = False

logger.info('This is a message from inside the helper module')

# create a file handler
stream_h = logging.StreamHandler() # This will log to the console
file_h = logging.FileHandler('file.log') # This will log to a file

# level and format
stream_h.setLevel(logging.WARNING) 
file_h.setLevel(logging.ERROR) 

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(stream_h)
logger.addHandler(file_h)