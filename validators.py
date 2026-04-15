import re

def validate_click_interval(interval):
    if not isinstance(interval, (int, float)):
        raise ValueError('Interval must be a number.')
    if interval <= 0:
        raise ValueError('Interval must be greater than zero.')


def validate_click_count(count):
    if not isinstance(count, int):
        raise ValueError('Click count must be an integer.')
    if count < 1:
        raise ValueError('Click count must be at least 1.')


def validate_coordinates(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValueError('Coordinates must be integers.')
    if not (0 <= x <= 1920 and 0 <= y <= 1080):
        raise ValueError('Coordinates must be within screen boundaries.')