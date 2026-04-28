import time
import threading
from queue import Queue

class ClickProcessor:
    def __init__(self, click_interval=0.1):
        self.click_interval = click_interval
        self.is_running = False
        self.queue = Queue()

    def start_auto_clicker(self):
        self.is_running = True
        threading.Thread(target=self._process_queue, daemon=True).start()

    def stop_auto_clicker(self):
        self.is_running = False

    def _process_queue(self):
        while self.is_running:
            if not self.queue.empty():
                self._perform_click(self.queue.get_nowait())
            time.sleep(self.click_interval)

    def queue_click(self, click_coordinates):
        self.queue.put(click_coordinates)

    def _perform_click(self, coords):
        # Simulated click action at specified coordinates
        print(f"Clicking at {coords}")

if __name__ == '__main__':
    processor = ClickProcessor()
    processor.start_auto_clicker()
    processor.queue_click((100, 200))
    time.sleep(1)
    processor.queue_click((150, 250))
    time.sleep(1)
    processor.stop_auto_clicker()