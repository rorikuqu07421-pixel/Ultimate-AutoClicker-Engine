"""
Configuration settings for the Ultimate-AutoClicker-Engine.

This module defines all necessary configurations, including default
values for application settings, paths for resources, and any other
parameters that affect the operation of the application.

Attributes:
    DEFAULT_CLICK_INTERVAL (int): The default interval between clicks.
    DEFAULT_CLICKS (int): The default number of clicks to perform.
    RESOURCE_PATH (str): Relative path to resource files.
"""

# Default time interval between clicks in milliseconds
DEFAULT_CLICK_INTERVAL: int = 100

# Default number of clicks to be executed
DEFAULT_CLICKS: int = 1000

# Path where resource files are located, adjust as necessary
RESOURCE_PATH: str = "resources/"


def get_config() -> dict:
    """
    Returns the application's configuration settings as a dictionary.

    The returned dictionary includes all configurable items, which can be
    modified by the user if necessary. This is useful for accessing the
    configuration items throughout the application in a convenient format.

    Returns:
        dict: A dictionary containing the configuration settings.
    """
    return {
        'click_interval': DEFAULT_CLICK_INTERVAL,
        'clicks': DEFAULT_CLICKS,
        'resource_path': RESOURCE_PATH
    }


if __name__ == '__main__':
    # Example usage of the configuration settings
    config = get_config()
    print(f"Current Configurations: {config}")
