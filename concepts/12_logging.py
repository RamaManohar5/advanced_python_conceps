"""
    The logging module in Python is a powerful built-in module so you can quickly add logging to your application.

"""
# There are 5 different log levels indicating the serverity of events.
# By default, the system logs only events with level WARNING and above.
import logging
logging.debug("this is a debug msg")
logging.info("this is a info msg")

logging.warning("this is a warning msg")
logging.error("this is a error msg")
logging.critical("this is a critical msg")

# Configuration¶
# With basicConfig(**kwargs) you can customize the root logger. 
# The most common parameters are the level, the format, and the filename. 
import logging
logging.basicConfig(level=logging.DEBUG, format='%(ascitime)s -%(name)s-%(levelname)s-%(message)s',\
                    datefmt='%m/%d/%Y %H:%M:%S')
# Now also debug messages will get logged with a different format.
logging.debug('Debug message')
# This would log to a file instead of the console.
logging.basicConfig(level=logging.DEBUG, filename='app.log')

# .conf file
# Create a .conf (or sometimes stored as .ini) file, define the loggers, handlers, and formatters and provide the names as keys. 
# After their names are defined, they are configured by adding the words logger, handler, and formatter before their names separated by an underscore.
# Then you can set the properties for each logger, handler, and formatter.

# Then use the config file in the code
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger with the name from the config file. 
# This logger now has StreamHandler with DEBUG Level and the specified format
logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')

# Rotating FileHandler
# When you have a large application that logs many events to a file, and you only need to keep track of the most recent events, then use a RotatingFileHandler that keeps the files small. 
# When the log reaches a certain number of bytes, it gets "rolled over". 
# You can also keep multiple backup log files before overwriting them.

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    pass
    # logger.info('Hello, world!')


# TimedRotatingFileHandler
# If your application will be running for a long time, you can use a TimedRotatingFileHandler.
# This will create a rotating log based on how much time has passed.
# Possible time conditions for the when parameter are: - second (s) - minute (m) - hour (h) - day (d) - w0-w6 (weekday, 0=Monday) - midnight
import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
logger.addHandler(handler)

for i in range(6):
    logger.info('Hello, world!')
    time.sleep(50)

#Logging in JSON Format
# If your application generates many logs from different modules, and especially in a microservice architecture, it can be challenging to locate the important logs for your analysis. 
# Therefore, it is best practice to log your messages in JSON format, and send them to a centralized log management system. 
# Then you can easily search, visualize, and analyze your log records.

# !pip install python-json-logger
'''
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

'''