import re

class InputValidator:
    @staticmethod
    def is_valid_click_interval(interval):
        if isinstance(interval, (int, float)) and interval > 0:
            return True
        raise ValueError("Click interval must be a positive number.")

    @staticmethod
    def is_valid_click_count(count):
        if isinstance(count, int) and count > 0:
            return True
        raise ValueError("Click count must be a positive integer.")

    @staticmethod
    def is_valid_key_sequence(sequence):
        if isinstance(sequence, str) and re.match(r'^[a-zA-Z0-9 ]+$', sequence):
            return True
        raise ValueError("Key sequence must be a valid alphanumeric string.")

    @staticmethod
    def validate_settings(interval, count, sequence):
        return (InputValidator.is_valid_click_interval(interval), 
                InputValidator.is_valid_click_count(count), 
                InputValidator.is_valid_key_sequence(sequence))
