from typing import Final

# Click intervals in milliseconds
CLICK_INTERVAL: Final[int] = 100
DOUBLE_CLICK_INTERVAL: Final[int] = 200

# Mouse button identifiers
LEFT_BUTTON: Final[int] = 1
RIGHT_BUTTON: Final[int] = 2
MIDDLE_BUTTON: Final[int] = 3

# Click types
class ClickType:
    SINGLE: Final[str] = 'single'
    DOUBLE: Final[str] = 'double'

# Default configuration
DEFAULT_CONFIG: Final[dict] = {
    'click_type': ClickType.SINGLE,
    'interval': CLICK_INTERVAL,
    'button': LEFT_BUTTON
}

def get_config() -> dict:
    """Returns the default click configuration."""
    return DEFAULT_CONFIG

