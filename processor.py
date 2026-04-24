import time
import threading

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self._run).start()

    def _run(self):
        while self.running:
            self.click()
            time.sleep(self.interval)

    def stop(self):
        self.running = False

    def click(self):
        # Simulating a click action
        print("Click!")

if __name__ == '__main__':
    auto_clicker = AutoClicker(interval=0.5)
    auto_clicker.start()
    time.sleep(5)
    auto_clicker.stop()