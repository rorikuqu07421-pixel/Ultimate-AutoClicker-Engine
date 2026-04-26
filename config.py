import json
import os

DEFAULT_CONFIG = {
    'click_interval': 100,
    'max_clicks': 1000,
    'click_duration': 10,
    'enabled': True
}

class ConfigurationLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                file_config = json.load(f)
                return {**DEFAULT_CONFIG, **file_config}
        return DEFAULT_CONFIG

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def update_config(self, new_config):
        self.config.update(new_config)
        self.save_config()

