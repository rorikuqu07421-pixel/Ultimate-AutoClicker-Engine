import time
import random

def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid type for division!")
        return None


def wait_random(seconds_min, seconds_max):
    try:
        if seconds_min < 0 or seconds_max < 0:
            raise ValueError("Wait times must be non-negative.")
        if seconds_min > seconds_max:
            raise ValueError("Minimum time cannot exceed maximum time.")
        time_to_wait = random.uniform(seconds_min, seconds_max)
        time.sleep(time_to_wait)
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def validate_click_position(position):
    if not isinstance(position, tuple) or len(position) != 2:
        print("Error: Position must be a tuple of (x, y).")
        return False
    x, y = position
    if not (isinstance(x, int) and isinstance(y, int)):
        print("Error: x and y must be integers.")
        return False
    return True
