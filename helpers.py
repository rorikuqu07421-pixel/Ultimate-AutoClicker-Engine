import time
import threading

class ClickHelper:
    def __init__(self, click_interval=0.1):
        self.click_interval = click_interval
        self._stop_event = threading.Event()

    def start_clicking(self):
        self._stop_event.clear()
        threading.Thread(target=self._click_loop).start()

    def stop_clicking(self):
        self._stop_event.set()

    def _click_loop(self):
        while not self._stop_event.is_set():
            self.perform_click()
            time.sleep(self.click_interval)

    @staticmethod
    def perform_click():
        # This is where you would integrate clicking functionality
        print('Clicked!')

if __name__ == '__main__':
    click_helper = ClickHelper(click_interval=0.2)
    click_helper.start_clicking()
    time.sleep(2)
    click_helper.stop_clicking()
