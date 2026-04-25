from typing import Callable, Optional
import time

class AutoClicker:
    def __init__(self, click_interval: float) -> None:
        """
        Initializes the AutoClicker with a specified interval between clicks.

        :param click_interval: Time in seconds between each simulated click.
        """
        self.click_interval = click_interval
        self.running = False

    def start_clicking(self, click_action: Callable, duration: Optional[float] = None) -> None:
        """
        Starts the auto-clicking process.

        :param click_action: A callable that performs the click action.
        :param duration: Optional duration in seconds; if specified, stops clicking after this duration.
        """
        self.running = True
        end_time = time.time() + duration if duration else None
        while self.running:
            click_action()
            time.sleep(self.click_interval)
            if end_time and time.time() >= end_time:
                break

    def stop_clicking(self) -> None:
        """
        Stops the auto-clicking process.
        """
        self.running = False

# Example click action function

def example_click():
    print("Clicked!")

# Example usage
if __name__ == '__main__':
    auto_clicker = AutoClicker(0.5)  # Click every 0.5 seconds
    # This will start clicking for 5 seconds
    auto_clicker.start_clicking(example_click, 5)