import time
import random

def validate_input(user_input, valid_range):
    if not isinstance(user_input, (int, float)):
        raise ValueError('Input must be a number')
    if not (valid_range[0] <= user_input <= valid_range[1]):
        raise ValueError(f'Input must be between {valid_range[0]} and {valid_range[1]}')

def auto_clicker_loop(click_interval, duration):
    validate_input(click_interval, (0.01, 5))
    validate_input(duration, (1, 3600))
    end_time = time.time() + duration
    while time.time() < end_time:
        print('Click!')  # Simulate click action
        time.sleep(click_interval)
        
if __name__ == '__main__':
    try:
        auto_clicker_loop(0.5, 10)
    except ValueError as e:
        print(f'Error: {e}')