import logging

logger = logging.getLogger("UltimateAutoClicker")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("app.log", mode='a')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def log_info(message: str) -> None:
    """
    Logs an informational message.
    
    Args:
        message (str): The message to log.
    """
    logger.info(message)


def log_error(message: str) -> None:
    """
    Logs an error message.
    
    Args:
        message (str): The message to log.
    """
    logger.error(message)


def log_debug(message: str) -> None:
    """
    Logs a debug message.
    
    Args:
        message (str): The message to log.
    """
    logger.debug(message)