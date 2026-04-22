import logging

# Configuring the logger
logger = logging.getLogger('AutoClickerLogger')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('autoclicker.log')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

def log_click_event(click_data):
    if not isinstance(click_data, dict):
        logger.error('Invalid click data format')
        return
    logger.info('Click event recorded: %s', click_data)


def log_error(error_message):
    logger.error('Error occurred: %s', error_message)


def log_info(info_message):
    logger.info('Info: %s', info_message)