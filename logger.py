import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=10*1024*1024, backup_count=5):
    logger = logging.getLogger('AutoClickerLogger')
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        # Create a directory for logs if it doesn't exist
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger

if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up successfully!')
    log.debug('This is a debug message.')
    log.error('This is an error message.')
