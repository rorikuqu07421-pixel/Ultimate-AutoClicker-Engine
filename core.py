import time
import threading

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.running = False
        self.click_thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.click_thread = threading.Thread(target=self._click)
            self.click_thread.start()

    def _click(self):
        while self.running:
            self.perform_click()
            time.sleep(self.interval)

    def stop(self):
        self.running = False
        if self.click_thread:
            self.click_thread.join()

    def perform_click(self):
        # Here, we would place the actual clicking logic
        print('Click!')  # Placeholder for actual click action
    
# Example usage
if __name__ == '__main__':
    autoclicker = AutoClicker(interval=0.05)
    autoclicker.start()
    time.sleep(1)  # Let it click for a second
    autoclicker.stop()