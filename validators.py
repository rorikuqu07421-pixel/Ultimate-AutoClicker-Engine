import re

class ValidationError(Exception):
    pass

def validate_click_rate(rate):
    if not isinstance(rate, (int, float)):
        raise ValidationError('Click rate must be a number.')
    if rate <= 0:
        raise ValidationError('Click rate must be greater than zero.')

def validate_duration(duration):
    if not isinstance(duration, (int, float)):
        raise ValidationError('Duration must be a number.')
    if duration < 0:
        raise ValidationError('Duration cannot be negative.')

def validate_coordinates(coordinates):
    if not isinstance(coordinates, tuple) or len(coordinates) != 2:
        raise ValidationError('Coordinates must be a tuple of two elements.')
    if not all(isinstance(coord, int) for coord in coordinates):
        raise ValidationError('Coordinates must be integers.')
    if not (0 <= coordinates[0] <= 1920) or not (0 <= coordinates[1] <= 1080):
        raise ValidationError('Coordinates must be within screen boundaries (0-1920, 0-1080).')

def validate_configuration(config):
    validate_click_rate(config.get('click_rate', 1))
    validate_duration(config.get('duration', 1))
    validate_coordinates(config.get('coordinates', (0, 0)))