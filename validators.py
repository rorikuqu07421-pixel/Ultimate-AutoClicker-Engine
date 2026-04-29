import re

def is_valid_click_speed(speed):
    """Validate click speed value."""
    return isinstance(speed, (int, float)) and speed > 0


def is_valid_click_count(count):
    """Validate click count value."""
    return isinstance(count, int) and count > 0


def is_valid_hotkey(hotkey):
    """Validate if the hotkey format is correct."""
    return bool(re.match(r'^[a-zA-Z]+$', hotkey))


def validate_config(config):
    """Validate the autoclicker configuration parameters."""
    errors = []
    if not is_valid_click_speed(config.get('click_speed', 0)):
        errors.append('Invalid click speed')
    if not is_valid_click_count(config.get('click_count', 0)):
        errors.append('Invalid click count')
    if not is_valid_hotkey(config.get('hotkey', '')):
        errors.append('Invalid hotkey format')
    if errors:
        raise ValueError(', '.join(errors))

