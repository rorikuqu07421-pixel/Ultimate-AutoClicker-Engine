import json
import os

DEFAULTS = {
    'click_interval': 0.1,
    'max_clicks': 1000,
    'duration': 10,
    'enabled': True
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULTS.copy()
        self.load_config()

    def load_config(self):
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.config)