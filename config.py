import os
import json

class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            default_config = self.create_default_config()
            self.save_config(default_config)
            return default_config
        with open(self.config_file, 'r') as f:
            return json.load(f)

    def save_config(self, config):
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)

    def create_default_config(self):
        return {
            'click_interval': 0.1,
            'max_clicks': 100,
            'click_button': 'left',
            'enabled': True
        }

    def update_config(self, key, value):
        if key in self.settings:
            self.settings[key] = value
            self.save_config(self.settings)
        else:
            raise KeyError(f'Key {key} not found in config.')