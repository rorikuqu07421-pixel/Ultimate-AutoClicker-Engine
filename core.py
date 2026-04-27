import time
import threading
from typing import Callable

class AutoClicker:
    def __init__(self, click_interval: float, click_action: Callable[[], None]) -> None:
        """Initialize an AutoClicker instance.

        Args:
            click_interval (float): Time interval between clicks in seconds.
            click_action (Callable[[], None]): Function to execute on each click.
        """
        self.click_interval = click_interval
        self.click_action = click_action
        self.running = False
        self.thread = threading.Thread(target=self._run)

    def start(self) -> None:
        """Start the auto-clicker thread."""
        self.running = True
        self.thread.start()

    def stop(self) -> None:
        """Stop the auto-clicker thread."""
        self.running = False
        self.thread.join()

    def _run(self) -> None:
        while self.running:
            self.click_action()
            time.sleep(self.click_interval)

# Example usage:
if __name__ == '__main__':
    def example_click():
        print('Clicked!')

    clicker = AutoClicker(1.0, example_click)
    clicker.start()
    time.sleep(5)
    clicker.stop()
