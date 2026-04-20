import time
import threading

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.clicking = False
        self.thread = None

    def start_clicking(self):
        if not self.clicking:
            self.clicking = True
            self.thread = threading.Thread(target=self._click_loop)
            self.thread.start()

    def stop_clicking(self):
        if self.clicking:
            self.clicking = False
            self.thread.join()

    def _click_loop(self):
        while self.clicking:
            self._perform_click()
            time.sleep(self.interval)

    def _perform_click(self):
        # Simulate a click event
        print('Click!')

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.05)
    clicker.start_clicking()
    time.sleep(1)
    clicker.stop_clicking()