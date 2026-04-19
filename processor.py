from typing import List, Dict, Any
import time

def process_clicks(clicks: List[Dict[str, Any]], interval: float) -> None:
    """Processes a list of clicks with a specified interval.

    Args:
        clicks (List[Dict[str, Any]]): A list of dictionaries where each dictionary represents a click event.
        interval (float): Time in seconds to wait between clicks.
    """
    for click in clicks:
        if 'x' in click and 'y' in click:
            click_position(click['x'], click['y'])
            time.sleep(interval)
        else:
            raise ValueError("Each click must contain 'x' and 'y' coordinates.")


def click_position(x: int, y: int) -> None:
    """Simulates a mouse click at a given position.

    Args:
        x (int): The x-coordinate for the click.
        y (int): The y-coordinate for the click.
    """
    print(f"Clicking at position: ({x}, {y})")
    # Here you would integrate actual mouse click functionality


def main() -> None:
    """Main function to simulate clicks.
    """
    clicks = [{'x': 100, 'y': 200}, {'x': 150, 'y': 250}]
    process_clicks(clicks, 0.5)

if __name__ == '__main__':
    main()