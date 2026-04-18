import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=3):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger

if __name__ == '__main__':
    my_logger = setup_logger(log_file='app.log')
    my_logger.info('Logger is set up and ready to use!')