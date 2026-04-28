import time
import threading

class Clicker:
    def __init__(self, interval):
        self.interval = interval
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.click_thread = threading.Thread(target=self._click_loop)
            self.click_thread.start()

    def _click_loop(self):
        while self.is_running:
            self._perform_click()
            time.sleep(self.interval)

    def _perform_click(self):
        print('Click!')  # Simulate a mouse click

    def stop(self):
        self.is_running = False
        self.click_thread.join()

if __name__ == '__main__':
    clicker = Clicker(1)
    clicker.start()
    time.sleep(5)
    clicker.stop()
