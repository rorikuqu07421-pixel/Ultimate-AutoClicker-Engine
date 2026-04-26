import threading
import time

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.active = False
        self._thread = None

    def start(self):
        if not self.active:
            self.active = True
            self._thread = threading.Thread(target=self._clicking)
            self._thread.start()

    def stop(self):
        if self.active:
            self.active = False
            self._thread.join()

    def _clicking(self):
        while self.active:
            self.perform_click()
            time.sleep(self.interval)

    def perform_click(self):
        print("Click!") # Simulate click action

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.05)
    try:
        clicker.start()
        time.sleep(1)  # Click for 1 second
    finally:
        clicker.stop()  # Ensure we stop the clicker
