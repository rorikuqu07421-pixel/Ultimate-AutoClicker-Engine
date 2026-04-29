import logging
import os
import sys

class Logger:
    def __init__(self, name, log_file='app.log', level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.log_file = log_file
        self.handler = self._create_handler()
        self.logger.addHandler(self.handler)

    def _create_handler(self):
        if not os.path.exists(os.path.dirname(self.log_file)):
            try:
                os.makedirs(os.path.dirname(self.log_file))
            except Exception as e:
                self.logger.error(f'Failed to create log directory: {str(e)}')
                sys.exit(1)
        handler = logging.FileHandler(self.log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        return handler

    def log_info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            self.logger.error(f'Failed to log info: {str(e)}')

    def log_error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            self.logger.critical(f'Failed to log error: {str(e)}')

    def log_warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            self.logger.critical(f'Failed to log warning: {str(e)}')

    def close(self):
        for handler in self.logger.handlers:
            handler.close()
            self.logger.removeHandler(handler)