import json

DEFAULT_CONFIG = {
    'click_interval': 0.1,
    'max_clicks': 100,
    'click_type': 'left',
    'click_position': [0, 0],
    'enabled': True
}

class ConfigLoader:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.filename, 'r') as config_file:
                user_config = json.load(config_file)
                return {**DEFAULT_CONFIG, **user_config}
        except FileNotFoundError:
            return DEFAULT_CONFIG
        except json.JSONDecodeError:
            print('Error loading config, using defaults.')
            return DEFAULT_CONFIG

if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.config)