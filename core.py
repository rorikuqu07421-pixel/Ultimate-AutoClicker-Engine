import time
import threading
from queue import Queue

class AutoClicker:
    def __init__(self, interval, limit):
        self.interval = interval
        self.limit = limit
        self.clicks = Queue()
        self.running = False

    def start_clicking(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self._click).start()

    def _click(self):
        count = 0
        while self.running and count < self.limit:
            self.clicks.put('click')  # Simulate a click
            time.sleep(self.interval)
            count += 1

    def stop_clicking(self):
        self.running = False

    def get_clicks_count(self):
        return self.clicks.qsize()

    def clear_clicks(self):
        self.clicks.queue.clear()

if __name__ == '__main__':
    ac = AutoClicker(0.1, 10)  # 10 clicks at 0.1 seconds
    ac.start_clicking()
    time.sleep(1)
    print('Total clicks:', ac.get_clicks_count())
    ac.stop_clicking()
