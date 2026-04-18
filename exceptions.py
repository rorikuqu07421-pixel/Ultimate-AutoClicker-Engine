class AutoClickerError(Exception):
    """Base class for all autoclicker errors."""

class ConfigurationError(AutoClickerError):
    """Raised when there is a configuration error."""
    def __init__(self, message, config_item=None):
        self.config_item = config_item
        super().__init__(message)

class ClickerDelayError(AutoClickerError):
    """Raised when a click delay is invalid."""
    def __init__(self, delay):
        self.delay = delay
        message = f'Invalid click delay: {delay}. Must be a positive number.'
        super().__init__(message)

class ClickCountError(AutoClickerError):
    """Raised when click count is invalid."""
    def __init__(self, count):
        self.count = count
        message = f'Invalid click count: {count}. Must be a positive integer.'
        super().__init__(message)

class ClickerNotActiveError(AutoClickerError):
    """Raised when clicker is not active."""
    def __init__(self):
        message = 'Clicker must be active to perform this action.'
        super().__init__(message)