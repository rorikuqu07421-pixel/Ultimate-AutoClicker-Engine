import json
import os

DEFAULT_CONFIG = {
    'click_interval': 0.1,
    'max_clicks': 1000,
    'enabled': True,
    'click_type': 'left',
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                config = json.load(file)
                return self.merge_configs(DEFAULT_CONFIG, config)
        return DEFAULT_CONFIG

    def merge_configs(self, defaults, custom):
        merged = defaults.copy()
        merged.update(custom)
        return merged

    def get(self, key, default=None):
        return self.config.get(key, default)
