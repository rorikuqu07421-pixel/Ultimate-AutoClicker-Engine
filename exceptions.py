class AutoClickerError(Exception):
    """Base class for all exceptions related to the AutoClicker engine."""
    pass

class ClickRateExceededError(AutoClickerError):
    """Raised when the click rate exceeds the maximum allowed rate."""
    def __init__(self, rate):
        super().__init__(f'Click rate {rate} exceeds maximum allowed rate.')
        self.rate = rate

class ConfigurationError(AutoClickerError):
    """Raised when there is an error in the configuration settings."""
    def __init__(self, message):
        super().__init__(message)

class InvalidClickTargetError(AutoClickerError):
    """Raised when the specified click target is invalid."""
    def __init__(self, target):
        super().__init__(f'Invalid click target specified: {target}')
        self.target = target

class ClickFrequencyError(AutoClickerError):
    """Raised when the click frequency is set incorrectly."""
    def __init__(self, frequency):
        super().__init__(f'Click frequency {frequency} is not valid.')
        self.frequency = frequency