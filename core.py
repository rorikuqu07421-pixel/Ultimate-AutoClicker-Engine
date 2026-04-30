import time
import json
import threading

class AutoClicker:
    def __init__(self, interval=1.0, click_count=10):
        self.interval = interval
        self.click_count = click_count
        self.is_running = False

    def start_clicking(self):
        if self.is_running:
            return
        self.is_running = True
        threading.Thread(target=self._click).start()

    def _click(self):
        for _ in range(self.click_count):
            if not self.is_running:
                break
            self.perform_click()
            time.sleep(self.interval)

    def stop_clicking(self):
        self.is_running = False

    def perform_click(self):
        # Simulate a click action
        print('Click!')

    def save_clicker_data(self, filename='clicker_data.json'):
        data = {'interval': self.interval, 'click_count': self.click_count}
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_clicker_data(self, filename='clicker_data.json'):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.interval = data['interval']
            self.click_count = data['click_count']

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5, click_count=5)
    clicker.start_clicking()
    time.sleep(3)
    clicker.stop_clicking()
    clicker.save_clicker_data()
    clicker.load_clicker_data()