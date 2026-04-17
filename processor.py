from typing import Callable, Optional
import time

class AutoClicker:
    def __init__(self, click_interval: float) -> None:
        """Initialize the AutoClicker with the specified click interval."
        self.click_interval = click_interval
        self.running = False

    def start(self) -> None:
        """Start the auto-clicking process."
        self.running = True
        print("AutoClicker started.")
        while self.running:
            self.perform_click()
            time.sleep(self.click_interval)

    def stop(self) -> None:
        """Stop the auto-clicking process."
        self.running = False
        print("AutoClicker stopped.")

    def perform_click(self) -> None:
        """Simulate a click action."
        print("Click!")

    def set_click_action(self, click_action: Callable[[], None]) -> None:
        """Set a custom click action to be executed."
        self.click_action = click_action

    def execute_click_action(self) -> None:
        """Execute the predefined click action."
        if hasattr(self, 'click_action'):
            self.click_action()  # Execute the custom action if defined.
        else:
            self.perform_click()  # Fallback to default click action.

# Example usage:
# auto_clicker = AutoClicker(1)
# auto_clicker.start()  # This would start clicking every 1 second
