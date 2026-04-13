import time
from threading import Thread, Event
from typing import Callable, Optional

class AutoClicker:
    """
    A class that implements an auto clicker functionality.
    
    Attributes:
        interval (float): Time in seconds between clicks.
        running (Event): An event used to control the sound repetition loop.
        click_function (Callable): The function that performs the clicking action.
    """

    def __init__(self, interval: float = 0.1, click_function: Optional[Callable] = None) -> None:
        """
        Initializes the AutoClicker with the specified interval and click function.
        
        Args:
            interval (float): Time in seconds between clicks. Defaults to 0.1 seconds.
            click_function (Callable): The actual function to be executed on each click.
        """
        self.interval = interval
        self.running = Event()
        self.click_function = click_function if click_function is not None else self.default_click

    def default_click(self) -> None:
        """
        A default click function that simulates a mouse click.
        This method can be overridden by a user-defined function.
        """
        print('Click!')  # In a real implementation, this would simulate a mouse click.

    def start(self) -> None:
        """
        Starts the auto clicking process in a separate thread.
        The clicking will continue until stopped.
        """
        self.running.set()
        Thread(target=self._click_loop, daemon=True).start()

    def _click_loop(self) -> None:
        """
        The main loop that performs the auto clicking action.
        This method runs in a separate thread and will
        continuously click at the set interval as long as running is True.
        """
        while self.running.is_set():
            start_time = time.time()
            self.click_function()  # Executes click function
            time_to_wait = self.interval - (time.time() - start_time)
            if time_to_wait > 0:
                time.sleep(time_to_wait)

    def stop(self) -> None:
        """
        Stops the auto clicking process safely.
        This method sets the running event to false, allowing the loop to exit.
        """
        self.running.clear()

# Example usage of the AutoClicker
if __name__ == '__main__':
    clicker = AutoClicker(interval=0.2)
    clicker.start()  # Start the auto clicker
    time.sleep(5)  # Let it run for 5 seconds
    clicker.stop()  # Stop the auto clicker
