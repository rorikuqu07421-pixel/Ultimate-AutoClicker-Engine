class AutoClickerError(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidConfigurationError(AutoClickerError):
    """Raised when the configuration is invalid."""
    def __init__(self, message):
        super().__init__(message)

class ClickRateExceededError(AutoClickerError):
    """Raised when the click rate exceeds the limit."""
    def __init__(self, rate):
        self.rate = rate
        message = f"Click rate {rate} exceeds limit."
        super().__init__(message)

class ActionNotAllowedError(AutoClickerError):
    """Raised when an action is not permitted."""
    def __init__(self, action):
        self.action = action
        message = f"Action '{action}' is not allowed."
        super().__init__(message)

class ClickerNotInitializedError(AutoClickerError):
    """Raised when trying to use clicker that hasn't been initialized."""
    def __init__(self):
        super().__init__("Clicker has not been initialized.")