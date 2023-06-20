# logging

```python
import logging
```



```python 
# initialize a logger 
# give the logger with the same name of the file
logger = logging.getLogger(__name__)
```



```python
logger.setLevel()
```

A statement that sets the logging level.

different logging levels could be choose:

* loggging.DEBUG
* logging.INFO
* logging.WARNING
* logging.ERROR
* logging.CRITICAL

If we set up logger.setLevel(**logging.INFO**), which means only the logs with higher levels (**INFO,WARNING,ERROR,CRITICAL**) would be recorded except of **DEBUG**.

## create logger 

```python
# build logger
logger = logging.getLogger(__name__) # also could give a name for the logger: "test_logger"

logger.setLevel(logging.INFO) # 设置日志记录级别的语句。它用于设置日志记录器（logger）对象的级别

# disable log message propagation to parent loggers
logger.propagate = False
```





```python
# build logger
logger=logging.getLogger('cash_rate_logger')
logger.setLevel(logging.INFO)

# disable log message propagation to parent loggers
logger.propagate = False

# log formats
console_handler=logging.StreamHandler()
logger.addHandler(console_handler)

console_formatter=logging.Formatter('[%(levelname)s]\t%(message)s')
console_handler.setFormatter(console_formatter)
```

