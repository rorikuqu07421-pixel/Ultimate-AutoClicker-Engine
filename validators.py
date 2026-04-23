from typing import Tuple, Union


def validate_coordinates(coordinates: Tuple[int, int]) -> bool:
    """
    Validates if the given coordinates are within the bounds of the screen.

    Args:
        coordinates (Tuple[int, int]): A tuple containing x and y coordinates.

    Returns:
        bool: True if coordinates are valid, False otherwise.
    """
    x, y = coordinates
    return 0 <= x <= 1920 and 0 <= y <= 1080


def validate_click_frequency(frequency: Union[int, float]) -> bool:
    """
    Validates whether the click frequency is a positive number.

    Args:
        frequency (Union[int, float]): The click frequency to validate.

    Returns:
        bool: True if frequency is positive, False otherwise.
    """
    return isinstance(frequency, (int, float)) and frequency > 0


def validate_delay(delay: Union[int, float]) -> bool:
    """
    Validates whether the delay is a non-negative number.

    Args:
        delay (Union[int, float]): The delay to validate.

    Returns:
        bool: True if delay is non-negative, False otherwise.
    """
    return isinstance(delay, (int, float)) and delay >= 0
