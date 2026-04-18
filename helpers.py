import random
import time

def click_mouse(x, y, button='left'):
    """Simulates a mouse click at (x, y) position."""
    # Import pyautogui or any suitable library
    import pyautogui
    if button not in ['left', 'right']:
        raise ValueError('Button must be left or right')
    pyautogui.click(x, y, button=button)


def random_delay(start=0.1, end=0.5):
    """Returns a random delay between start and end seconds."""
    return random.uniform(start, end)


def perform_clicks(num_clicks, x, y, delay_range=(0.1, 0.5), button='left'):
    """Performs multiple clicks with random delays."""
    for _ in range(num_clicks):
        click_mouse(x, y, button)
        time.sleep(random_delay(*delay_range))


def repeat_action(action, times):
    """Repeats an action for a specified number of times."""
    for _ in range(times):
        action()