import logging
'''
goal: logs with level WARNING and above to be logged to the console, but everything with level ERROR and above to be saved in a file
'''
# create a custom logger -> example_logger
logger = logging.getLogger(__name__)

# create handlers
# console log handler
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.WARNING)
# file log handler
f_handler = logging.FileHandler('file.log')
f_handler.setLevel(logging.ERROR)

# create formatters and add to the handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')