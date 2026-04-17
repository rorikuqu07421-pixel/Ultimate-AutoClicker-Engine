class AutoClickerError(Exception):
    """Base class for exceptions in the AutoClicker module."""
    pass

class ConfigurationError(AutoClickerError):
    """Raised for errors in configuration settings."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ClickRateError(AutoClickerError):
    """Raised when click rate is invalid."""
    def __init__(self, rate):
        self.rate = rate
        self.message = f"Invalid click rate: {self.rate}."
        super().__init__(self.message)

class TimeoutError(AutoClickerError):
    """Raised when an operation times out."""
    def __init__(self, timeout):
        self.timeout = timeout
        self.message = f"Operation timed out after {self.timeout} seconds."
        super().__init__(self.message)

class NotConfiguredError(AutoClickerError):
    """Raised when the autoclicker is not configured properly."""
    def __init__(self):
        self.message = "The AutoClicker has not been configured."
        super().__init__(self.message)

__all__ = [
    'AutoClickerError',
    'ConfigurationError',
    'ClickRateError',
    'TimeoutError',
    'NotConfiguredError'
]