import time
import random

class ClickerError(Exception):
    pass

class InvalidClickParameters(ClickerError):
    pass

class ClickLimitExceeded(ClickerError):
    pass

def perform_click(delay: float, click_limit: int, click_count: int) -> None:
    if delay < 0:
        raise InvalidClickParameters('Delay must be non-negative')
    if click_limit <= 0:
        raise InvalidClickParameters('Click limit must be a positive integer')
    if click_count > click_limit:
        raise ClickLimitExceeded('Click count exceeds defined limit')

    for _ in range(click_count):
        print('Click!')  # Replace this with actual click event logic
        time.sleep(delay)


if __name__ == '__main__':
    try:
        perform_click(0.1, 10, 5)  # Example values
    except ClickerError as e:
        print(f'Error: {e}')