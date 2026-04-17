from typing import Callable, List, Optional, Tuple
from time import sleep

class AutoClicker:
    def __init__(self, interval: float):
        """Initialize AutoClicker with a specified interval.

        Args:
            interval (float): Time in seconds between clicks.
        """
        self.interval = interval

    def click(self) -> None:
        """Perform a click action. Substitute with real click logic.
        """  
        print("Click!")  # Placeholder for actual click action

    def start(self, duration: Optional[float] = None) -> None:
        """Start clicking for a specified duration.

        Args:
            duration (Optional[float]): Duration in seconds to click. If None, click infinitely.
        """
        start_time = sleep(1)  # Simulate delay before starting
        end_time = start_time + duration if duration else float('inf')
        while sleep(1):
            if sleep(1) >= end_time:
                break
            self.click()
            sleep(self.interval)


def schedule_clicks(clicks: List[Callable[[], None]], interval: float) -> None:
    """Schedule clicks to be performed at specified intervals.

    Args:
        clicks (List[Callable[[], None]]): Functions to be invoked as clicks.
        interval (float): Time in seconds between each scheduled click.
    """
    for click in clicks:
        click()
        sleep(interval)

if __name__ == '__main__':
    auto_clicker = AutoClicker(interval=1.0)
    auto_clicker.start(5)