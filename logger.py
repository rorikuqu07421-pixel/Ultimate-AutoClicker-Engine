import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('autoclicker.log'),
        logging.StreamHandler()
    ]
)

class AutoClickerLogger:
    def __init__(self, name='AutoClicker'):
        self.logger = logging.getLogger(name)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_critical(self, message):
        self.logger.critical(message)

logger = AutoClickerLogger()
logger.log_info('AutoClicker started')
