import random
import time
import logging

class ClickerError(Exception):
    pass

class Clicker:
    def __init__(self, delay: float = 0.1, click_count: int = 10):
        if delay <= 0:
            raise ClickerError("Delay must be greater than 0")
        if click_count <= 0:
            raise ClickerError("Click count must be greater than 0")
        self.delay = delay
        self.click_count = click_count

    def perform_clicks(self):
        try:
            for _ in range(self.click_count):
                self.click()
                time.sleep(self.delay)
        except Exception as e:
            logging.error(f"An error occurred during clicking: {e}")

    def click(self):
        if random.random() < 0.05:
            raise ClickerError("Failed to perform click due to random error")
        print("Click!")

if __name__ == '__main__':
    try:
        my_clicker = Clicker(delay=0.1, click_count=5)
        my_clicker.perform_clicks()
    except ClickerError as e:
        logging.error(f"Clicker initialization failed: {e}")
    except Exception as general_error:
        logging.error(f"An unexpected error occurred: {general_error}")