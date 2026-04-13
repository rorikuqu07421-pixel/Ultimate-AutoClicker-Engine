import time
import threading
from typing import Callable, Optional

class AutoClicker:
    """
    A class that implements an auto-clicker functionality,
    allowing users to automate mouse clicks based on specified
    parameters such as clicks per second and duration.
    """

    def __init__(self, clicks_per_second: float, duration: Optional[int] = None) -> None:
        """
        Initializes the AutoClicker with specified parameters.

        Args:
            clicks_per_second (float): The number of clicks to perform per second.
            duration (Optional[int]): Total duration in seconds for which to run the
                                      auto-clicker. If None, runs indefinitely.
        """
        self.clicks_per_second = clicks_per_second
        self.duration = duration
        self.running = False
        self.thread = None

    def start(self) -> None:
        """
        Starts the auto-clicking process in a new thread.
        Calculates the interval between clicks and ensures that
        the clicking stops after the specified duration, if provided.
        """ 
        if self.running:
            print("AutoClicker is already running.")
            return

        self.running = True
        self.thread = threading.Thread(target=self._click)
        self.thread.start()

    def stop(self) -> None:
        """
        Stops the auto-clicking process gracefully.
        """ 
        if not self.running:
            print("AutoClicker is not running.")
            return

        self.running = False
        self.thread.join()  # Ensures the thread has finished

    def _click(self) -> None:
        """
        Private method that performs the clicking action based on
        the clicks per second rate and duration.

        Uses a while loop to continue clicking until the duration
        has elapsed (if specified), or until it's manually stopped.
        """
        click_interval = 1 / self.clicks_per_second  # Calculate interval
        start_time = time.time()  # Record the start time

        while self.running:
            print("Click!")  # Here we would actually perform a click
            time.sleep(click_interval)  # Wait for the interval
            if self.duration is not None and (time.time() - start_time) >= self.duration:
                break  # Stop if duration has elapsed

        self.running = False  # Set running to False when done
        print("AutoClicker has stopped.")
