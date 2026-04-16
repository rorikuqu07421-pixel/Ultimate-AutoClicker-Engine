import time
import threading

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.running = False
        self.clicks = 0

    def start(self):
        self.running = True
        threading.Thread(target=self._run).start()

    def _run(self):
        while self.running:
            self.perform_click()
            time.sleep(self.interval)

    def perform_click(self):
        # Simulated click action
        self.clicks += 1
        print(f"Click {self.clicks}")

    def stop(self):
        self.running = False

    def get_clicks(self):
        return self.clicks

if __name__ == '__main__':
    clicker = AutoClicker(0.05)
    clicker.start()
    time.sleep(1)
    clicker.stop()
    print(f'Total clicks: {clicker.get_clicks()}')