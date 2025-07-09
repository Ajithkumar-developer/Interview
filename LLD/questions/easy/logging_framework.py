# Designing a Logging Framework

# Requirements
# The logging framework should support different log levels, such as DEBUG, INFO, WARNING, ERROR, and FATAL.
# It should allow logging messages with a timestamp, log level, and message content.
# The framework should support multiple output destinations, such as console, file, and database.
# It should provide a configuration mechanism to set the log level and output destination.
# The logging framework should be thread-safe to handle concurrent logging from multiple threads.
# It should be extensible to accommodate new log levels and output destinations in the future.


import threading
import datetime
from enum import Enum
import sys

# === LogColors ===
LOG_COLORS = {
    'DEBUG': '\033[94m',    # Blue
    'INFO': '\033[92m',     # Green
    'WARNING': '\033[93m',  # Yellow
    'ERROR': '\033[91m',    # Red
    'FATAL': '\033[95m',    # Magenta
    'RESET': '\033[0m'      # Reset to default
}


# === LogLevel ===
class LogLevel(Enum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    FATAL = 50


# === LogRecord ===
class LogRecord:
    def __init__(self, level, message):
        self.timestamp = datetime.datetime.now()
        self.level = level
        self.message = message
        self.thread_id = threading.get_ident()

    def to_dict(self):
        return {
            'asctime': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'levelname': self.level.name,
            'message': self.message,
            'thread': self.thread_id
        }

    def __str__(self):
        return f"{self.timestamp} [{self.level.name}] (Thread-{self.thread_id}): {self.message}"


# === Formatter ===
class Formatter:
    def __init__(self, fmt="%(asctime)s - %(levelname)s - %(message)s"):
        self.fmt = fmt

    def format(self, record: LogRecord) -> str:
        record_dict = record.to_dict()
        try:
            return self.fmt % record_dict
        except KeyError as e:
            raise ValueError(f"Invalid format key: {e}") from e


# === Handlers ===
class BaseHandler:
    def __init__(self, formatter=None):
        self.formatter = formatter or Formatter()

    def emit(self, record: LogRecord):
        raise NotImplementedError


# class ConsoleHandler(BaseHandler):
#     def emit(self, record: LogRecord):
#         print(self.formatter.format(record), file=sys.stdout)

class ConsoleHandler(BaseHandler):
    def emit(self, record: LogRecord):
        level_name = record.level.name
        color = LOG_COLORS.get(level_name, "")
        reset = LOG_COLORS['RESET']
        formatted = self.formatter.format(record)
        print(f"{color}{formatted}{reset}", file=sys.stdout)

class FileHandler(BaseHandler):
    def __init__(self, filename, formatter=None):
        super().__init__(formatter)
        self.filename = filename
        self.lock = threading.Lock()

    def emit(self, record: LogRecord):
        with self.lock:
            with open(self.filename, 'a') as f:
                f.write(self.formatter.format(record) + '\n')


class DatabaseHandler(BaseHandler):
    def emit(self, record: LogRecord):
        # Simulate database log - Replace with actual DB logic
        print("[DB LOG]", self.formatter.format(record))


# === Logger Configuration ===
class LoggerConfig:
    def __init__(self, level=LogLevel.DEBUG, handlers=None):
        self.level = level
        self.handlers = handlers or []


# === Logger ===
class Logger:
    def __init__(self, config: LoggerConfig):
        self.config = config
        self._lock = threading.Lock()

    def _log(self, level, message):
        if level.value >= self.config.level.value:
            record = LogRecord(level, message)
            with self._lock:
                for handler in self.config.handlers:
                    handler.emit(record)

    def debug(self, message): self._log(LogLevel.DEBUG, message)
    def info(self, message): self._log(LogLevel.INFO, message)
    def warning(self, message): self._log(LogLevel.WARNING, message)
    def error(self, message): self._log(LogLevel.ERROR, message)
    def fatal(self, message): self._log(LogLevel.FATAL, message)

    def add_handler(self, handler: BaseHandler):
        with self._lock:
            self.config.handlers.append(handler)

    def set_level(self, level: LogLevel):
        with self._lock:
            self.config.level = level


# === Example Usage ===
if __name__ == "__main__":
    custom_formatter = Formatter("%(asctime)s - [%(levelname)s] - %(message)s")

    config = LoggerConfig(
        level=LogLevel.DEBUG,
        handlers=[
            ConsoleHandler(formatter=custom_formatter),
            # FileHandler("app.log", formatter=custom_formatter),
            # DatabaseHandler(formatter=custom_formatter)
        ]
    )

    logger = Logger(config)

    logger.debug("This is a debug message.")  # Will not be logged (level=INFO)
    logger.info("Application started.")
    logger.warning("Low disk space.")
    logger.error("An error occurred.")
    logger.fatal("System crash!")
