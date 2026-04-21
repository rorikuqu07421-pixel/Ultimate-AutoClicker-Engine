class AutoClickerError(Exception):
    pass

class InvalidClickRateError(AutoClickerError):
    def __init__(self, rate):
        self.rate = rate
        super().__init__(f"Invalid click rate: {rate}. Must be a positive number.")

class FrequencyOutOfBoundsError(AutoClickerError):
    def __init__(self, frequency):
        self.frequency = frequency
        super().__init__(f"Frequency '{frequency}' is out of allowed bounds.")

class ConfigurationError(AutoClickerError):
    def __init__(self, message):
        super().__init__(message)


def validate_click_rate(rate):
    if not isinstance(rate, (int, float)) or rate <= 0:
        raise InvalidClickRateError(rate)


def validate_frequency(frequency, min_freq=1, max_freq=100):
    if frequency < min_freq or frequency > max_freq:
        raise FrequencyOutOfBoundsError(frequency)


def validate_configuration(config):
    required_keys = ['click_rate', 'frequency']
    for key in required_keys:
        if key not in config:
            raise ConfigurationError(f'Missing required configuration key: {key}')
    validate_click_rate(config['click_rate'])
    validate_frequency(config['frequency'])