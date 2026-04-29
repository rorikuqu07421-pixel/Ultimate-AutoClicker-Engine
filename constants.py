from typing import Final, Dict

# Constants for the Auto Clicker Engine

CLICK_INTERVAL: Final[float] = 0.1  # Time in seconds between clicks
MAX_CLICKS: Final[int] = 1000  # Maximum number of clicks in a session
SCREEN_RESOLUTION: Final[Dict[str, int]] = {'width': 1920, 'height': 1080}  # Default screen resolution

# Default click settings
DEFAULT_SETTINGS: Final[Dict[str, float]] = {
    'click_interval': CLICK_INTERVAL,
    'max_clicks': MAX_CLICKS
}

def get_screen_size() -> Dict[str, int]:
    """Retrieve current screen resolution.

    Returns:
        Dict[str, int]: A dictionary containing 'width' and 'height' keys.
    """
    return SCREEN_RESOLUTION

def get_default_settings() -> Dict[str, float]:
    """Retrieve default settings for the clicker.

    Returns:
        Dict[str, float]: A dictionary of default clicker settings.
    """
    return DEFAULT_SETTINGS
