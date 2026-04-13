import time
import threading
from typing import Callable

class AutoClicker:
    def __init__(self, click_function: Callable[[], None], interval: float) -> None:
        """
        Initialize the AutoClicker instance.
        
        :param click_function: A callable function that will be executed on each click.
        :param interval: The time interval between consecutive clicks in seconds.
        """
        self.click_function = click_function
        self.interval = interval
        self.is_running = False
        self.thread = threading.Thread(target=self.run)

    def start(self) -> None:
        """
        Start the auto-clicker.
        If the auto-clicker is already running, this method does nothing.
        """        
        if not self.is_running:
            self.is_running = True
            self.thread.start()

    def stop(self) -> None:
        """
        Stop the auto-clicker.
        If the auto-clicker is not running, this method does nothing.
        """        
        if self.is_running:
            self.is_running = False
            self.thread.join()  # Ensure the thread finishes execution.

    def run(self) -> None:
        """
        The main loop that runs concurrently to trigger the click function at the specified interval.
        This method should only be called internally.
        """        
        while self.is_running:
            start_time = time.time()  # Record the start time of each click.
            self.click_function()  # Call the specified click function.
            elapsed_time = time.time() - start_time  # Calculate how long the click took.

            time_to_sleep = self.interval - elapsed_time
            if time_to_sleep > 0:
                time.sleep(time_to_sleep)  # Sleep to maintain the desired interval.

# Example of a click function to be passed to AutoClicker
def example_click():
    print("Clicked!")

# Usage of AutoClicker.
if __name__ == '__main__':
    ac = AutoClicker(example_click, 1.0)  # Set interval to 1 second.
    ac.start()  # Start clicking.
    time.sleep(5)  # Let it click for 5 seconds.
    ac.stop()  # Stop clicking.