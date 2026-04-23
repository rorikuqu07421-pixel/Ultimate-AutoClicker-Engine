class AutoClickerError(Exception):
    """Base class for all exceptions raised by the autoclicker."""
    pass

class ClickRateError(AutoClickerError):
    """Raised when the click rate is invalid."""
    def __init__(self, rate):
        self.rate = rate
        super().__init__(f'Invalid click rate: {rate}')

class ConfigurationError(AutoClickerError):
    """Raised when there's a configuration issue."""
    def __init__(self, message):
        self.message = message
        super().__init__(f'Configuration error: {message}')

class ClickLimitExceeded(AutoClickerError):
    """Raised when click limit is exceeded."""
    def __init__(self, limit):
        self.limit = limit
        super().__init__(f'Click limit exceeded: {limit}')

class InvalidMacroError(AutoClickerError):
    """Raised for invalid macro actions."""
    def __init__(self, action):
        self.action = action
        super().__init__(f'Invalid macro action: {action}')