# Python Logging
Python provides a logging system as a part of its standard library, so you can quickly add logging to your application. By logging useful data from the right places, you can not only debug errors easily but also use the data to analyze the performance of the application to plan for scaling or look at usage patterns to plan for marketing.

## The logging module
With the logging module imported, you can use something called a “logger” to log messages that you want to see. By default, there are 5 standard levels indicating the severity of events.  
* DEBUG
* INFO
* WARNING
* ERROR
* CRITICAL

The logging module provides you with a default logger that allows you to get started without needing much configuration. The corresponding methods for each level can be called as shown in `basic.py` whose output is:
```bash
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
```
The output shows the severity level before each message along with root, which is the name the logging module gives to its default logger.This format, which shows the level, name, and message separated by a colon (:), is the default output format that can be configured to include things like timestamp, line number, and other details.

Notice that the debug() and info() messages didn’t get logged. This is because, by default, the logging module logs the messages with a severity level of WARNING or above. You can change that by configuring the logging module to log events of all levels if you want. You can also define your own severity levels by changing configurations, but it is generally not recommended as it can cause confusion with logs of some third-party libraries that you might be using.

## Basic configurations
You can use the `basicConfig(**kwargs)` method to configure the logging. Some of the commonly used parameters for basicConfig() are the following:

* `level`: The root logger will be set to the specified severity level.
* `filename`: This specifies the file.
* `filemode`: If filename is given, the file is opened in this mode. The default is a, which means append.
* `format`: This is the format of the log message.

Calling `basicConfig()` to configure the root logger works only if the root logger has not been configured before. Basically, this function can only be called once.

## Formatting the output
Examples:
process id
```python
import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')
```
Output
```bash
18472-WARNING-This is a Warning
```
date and time info
```python
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')
```
Output
```
2021-12-29 19:44:49,712 - Admin logged in
```

## Logging variable data
```python
import logging

name = 'Daniel'

logging.error(f'{name} raised an error')
```
Output
```
ERROR:root:Daniel raised an error
```

## Capturing stack traces
The logging module also allows you to capture the full stack traces in an application. Exception information can be captured if the exc_info parameter is passed as True, and the logging functions are called like this:
```python
import logging

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)
```
```bash
ERROR:root:Exception occurred
Traceback (most recent call last):
  File "exceptions.py", line 6, in <module>
    c = a / b
ZeroDivisionError: division by zero
```
logging.exception() method, which logs a message with level ERROR and adds exception information to the message. To put it more simply, calling logging.exception() is like calling logging.error(exc_info=True). But since this method always dumps exception information, it should only be called from an exception handler. 

## Create custom logger
You can (and should) define your own logger by creating an object of the Logger class, especially if your application has multiple modules.The most commonly used classes defined in the logging module are the following:
* `Logger`: This is the class whose objects will be used in the application code directly to call the functions.
* `LogRecord`: Loggers automatically create LogRecord objects that have all the information related to the event being logged, like the name of the logger, the function, the line number, the message, and more.
* `Handler`: Handlers send the LogRecord to the required output destination, like the console or a file. Handler is a base for subclasses like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more. These subclasses send the logging outputs to corresponding destinations, like sys.stdout or a disk file.
* `Formatter`: This is where you specify the format of the output by specifying a string format that lists out the attributes that the output should contain.

Out of these, we mostly deal with the objects of the Logger class, which are instantiated using the module-level function logging.getLogger(name). Multiple calls to getLogger() with the same name will return a reference to the same Logger object, which saves us from passing the logger objects to every part where it’s needed. Here’s an example:
```python
import logging

logger = logging.getLogger('example_logger')
logger.warning('This is a warning')
```
```bash
This is a warning
```
This creates a custom logger named example_logger, but unlike the root logger, the name of a custom logger is not part of the default output format and has to be added to the configuration.Again, unlike the root logger, a custom logger can’t be configured using basicConfig(). You have to configure it using Handlers and Formatters:

### Using handlers
Handlers come into the picture when you want to configure your own loggers and send the logs to multiple places when they are generated. Handlers send the log messages to configured destinations like the standard output stream or a file or over HTTP or to your email via SMTP.A logger that you create can have more than one handler, which means you can set it up to be saved to a log file and also send it over email.