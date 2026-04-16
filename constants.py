class ClickerConstants:
    CLICK_INTERVAL = 0.01  # Time between clicks in seconds
    DEFAULT_CLICKS = 100  # Default number of clicks
    CLICKER_NAME = 'Ultimate AutoClicker'
    SUPPORTED_OS = ['Windows', 'Linux', 'Mac']
    MAX_CLICKS_PER_SECOND = 1000  # Max clicks allowed per second

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

class ErrorMessages:
    INVALID_CLICK_COUNT = 'Error: Invalid click count provided.'
    OS_NOT_SUPPORTED = 'Error: Operating system not supported.'
    CONFIG_LOAD_FAILED = 'Error: Failed to load configuration.'

# Usage:
# from constants import ClickerConstants, Colors, ErrorMessages
# print(f'{Colors.GREEN}Clicker Ready!{Colors.RESET}')