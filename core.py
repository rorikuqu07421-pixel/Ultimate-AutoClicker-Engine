import time
import threading

class AutoClicker:
    def __init__(self, click_interval):
        self.click_interval = click_interval
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._click_loop)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _click_loop(self):
        while self.running:
            self.simulate_click()
            time.sleep(self.click_interval)

    def simulate_click(self):
        # Simulate the click action (placeholder)
        print('Click!')

    def adjust_click_interval(self, new_interval):
        if new_interval > 0:
            self.click_interval = new_interval

if __name__ == '__main__':
    autoclicker = AutoClicker(0.1)
    autoclicker.start()
    time.sleep(1)
    autoclicker.adjust_click_interval(0.05)
    time.sleep(3)
    autoclicker.stop()