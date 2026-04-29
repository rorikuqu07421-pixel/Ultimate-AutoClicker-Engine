import time
import random
import threading

def click(x, y):
    print(f'Clicking at ({x}, {y})')
    # Simulated mouse click

def auto_clicker(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        x, y = random.randint(0, 1920), random.randint(0, 1080)
        click(x, y)
        time.sleep(interval)

class AutoClickerThread(threading.Thread):
    def __init__(self, interval, duration):
        super().__init__()
        self.interval = interval
        self.duration = duration
        self.daemon = True

    def run(self):
        auto_clicker(self.interval, self.duration)

if __name__ == '__main__':
    interval = 0.1  # 10 clicks per second
    duration = 5    # 5 seconds of clicking
    click_thread = AutoClickerThread(interval, duration)
    click_thread.start()
    click_thread.join()  # Wait for the clicking to finish
