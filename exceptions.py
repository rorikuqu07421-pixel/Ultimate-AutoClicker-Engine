class AutoClickerError(Exception):
    """Base class for all autoclicker exceptions."""
    pass

class ConfigurationError(AutoClickerError):
    """Exception raised for errors in the configuration."""
    def __init__(self, message):
        super().__init__(message)

class ClickTimeoutError(AutoClickerError):
    """Exception raised for click timeout issues."""
    def __init__(self, timeout):
        self.timeout = timeout
        super().__init__(f"Click operation timed out after {timeout} seconds.")

class InvalidClickPatternError(AutoClickerError):
    """Exception raised for invalid click patterns."""
    def __init__(self, pattern):
        self.pattern = pattern
        super().__init__(f"Invalid click pattern: {pattern}")

class OverloadError(AutoClickerError):
    """Exception raised when system overload occurs."""
    def __init__(self, load):
        self.load = load
        super().__init__(f"System is overloaded with load: {load}")

class ClickRateError(AutoClickerError):
    """Exception raised for errors in click rate."""
    def __init__(self, rate):
        self.rate = rate
        super().__init__(f"Invalid click rate: {rate}")