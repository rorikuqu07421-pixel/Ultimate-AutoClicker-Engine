from typing import Any, Dict, Union


def is_valid_click_rate(rate: Union[int, float]) -> bool:
    """
    Validate if the given click rate is a positive number.

    :param rate: The click rate to validate.
    :return: True if the rate is positive, else False.
    """
    return isinstance(rate, (int, float)) and rate > 0


def is_valid_click_position(position: Dict[str, Any]) -> bool:
    """
    Validate if the click position is a dictionary with 'x' and 'y' keys.

    :param position: The position dictionary to validate.
    :return: True if valid, else False.
    """
    return (isinstance(position, dict) and
            'x' in position and 'y' in position and
            isinstance(position['x'], (int, float)) and
            isinstance(position['y'], (int, float)))


def is_valid_interval(interval: Union[int, float]) -> bool:
    """
    Validate if the given interval is a positive number.

    :param interval: The time interval to validate.
    :return: True if the interval is positive, else False.
    """
    return isinstance(interval, (int, float)) and interval > 0