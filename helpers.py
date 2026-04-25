from typing import List, Dict, Any


def click_with_delay(clicks: int, delay: float) -> None:
    """
    Simulate a series of clicks with a specified delay.

    Args:
        clicks (int): The number of clicks to simulate.
        delay (float): The time in seconds to wait between clicks.
    """
    import time
    for _ in range(clicks):
        print("Click!")  # Placeholder for actual click action
        time.sleep(delay)


def create_click_config(clicks: List[int], delays: List[float]) -> List[Dict[str, Any]]:
    """
    Create a list of click configurations.

    Args:
        clicks (List[int]): A list of click counts.
        delays (List[float]): A list of corresponding delays.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries with click and delay configurations.
    """
    return [{"clicks": c, "delay": d} for c, d in zip(clicks, delays)]


def validate_clicks_and_delays(clicks: int, delay: float) -> bool:
    """
    Validate the number of clicks and delay.

    Args:
        clicks (int): The number of clicks to validate.
        delay (float): The delay value to validate.

    Returns:
        bool: True if valid, otherwise False.
    """
    return clicks > 0 and delay > 0.0
