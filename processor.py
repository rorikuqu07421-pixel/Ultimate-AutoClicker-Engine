import time
import random

class AutoClicker:
    def __init__(self, clicks_per_second):
        self.set_clicks_per_second(clicks_per_second)

    def set_clicks_per_second(self, cps):
        if not isinstance(cps, (int, float)):
            raise ValueError('Clicks per second must be a number.')
        if cps <= 0:
            raise ValueError('Clicks per second must be greater than zero.')
        self.clicks_per_second = cps

    def start_clicking(self):
        print(f'Starting auto-clicker at {self.clicks_per_second} clicks per second.')
        try:
            while True:
                self.perform_click()
                time.sleep(1 / self.clicks_per_second)
        except KeyboardInterrupt:
            print('Auto-clicker stopped.')

    def perform_click(self):
        # Simulating the click action
        print('Click!')

if __name__ == '__main__':
    cps = input('Enter clicks per second: ')
    try:
        cps = float(cps)
        auto_clicker = AutoClicker(cps)
        auto_clicker.start_clicking()
    except ValueError as e:
        print(f'Input error: {e}')