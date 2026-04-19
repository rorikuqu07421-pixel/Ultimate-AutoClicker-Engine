import time
import threading
import random
import sys

class AutoClicker:
    def __init__(self, delay=0.1):
        self.delay = delay
        self.running = False

    def start(self):
        if self.running:
            raise RuntimeError('AutoClicker is already running!')
        self.running = True
        threading.Thread(target=self.click_loop).start()

    def stop(self):
        if not self.running:
            raise RuntimeError('AutoClicker is not running!')
        self.running = False

    def click_loop(self):
        try:
            while self.running:
                self.perform_click()
                time.sleep(self.delay)
        except Exception as e:
            print(f'Error in click loop: {e}')  
            self.stop()

    def perform_click(self):
        # Simulating click with a print statement
        print('Click!')

    def set_delay(self, new_delay):
        if new_delay < 0:
            raise ValueError('Delay must be a non-negative value.')
        self.delay = new_delay

if __name__ == '__main__':
    clicker = AutoClicker()
    try:
        clicker.start()
        time.sleep(random.randint(1, 5))  # let it click for a while
    except Exception as e:
        print(f'Error: {e}')
    finally:
        clicker.stop()