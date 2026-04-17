import json
import os

DEFAULT_CONFIG = {
    'click_interval': 100,
    'max_clicks': 1000,
    'enabled': False,
    'output_file': 'output.txt',
}

class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        self.load_config()

    def load_config(self):
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)

    def get(self, key):
        return self.config.get(key, DEFAULT_CONFIG.get(key))

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
