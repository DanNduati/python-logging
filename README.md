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