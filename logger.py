import logging
from typing import Any, Optional


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures a logger with a specific name and level.
    
    Args:
        name (str): The name of the logger.
        level (int): The logging level (default: logging.INFO).
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)  
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


def log_message(logger: logging.Logger, message: str, level: Optional[int] = None) -> None:
    """
    Logs a message with the specified logger at the given level.
    
    Args:
        logger (logging.Logger): The logger to use.
        message (str): The message to log.
        level (Optional[int]): The logging level (default: None, using logger's level).
    """
    if level:
        logger.log(level, message)
    else:
        logger.info(message)