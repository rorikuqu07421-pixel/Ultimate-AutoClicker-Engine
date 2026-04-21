import time
import random

class AutoClicker:
    def __init__(self, interval=1.0):
        self.interval = interval

    def click(self):
        print("Mouse clicked!")  # Simulating a mouse click

    def start_clicking(self, count):
        for _ in range(count):
            self.click()
            time.sleep(self.interval)

    def random_clicks(self, count):
        for _ in range(count):
            self.click()
            time.sleep(random.uniform(0.1, self.interval))

    @staticmethod
    def simulate_clicks(start_count=5, end_count=10):
        return random.randint(start_count, end_count)

if __name__ == '__main__':
    ac = AutoClicker(interval=0.5)
    click_count = ac.simulate_clicks()
    ac.start_clicking(click_count)