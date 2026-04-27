import json
import os

def load_config(filepath, default_config):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return json.load(file)
    else:
        return default_config

if __name__ == '__main__':
    defaults = {
        'click_speed': 0.1,
        'click_count': 100,
        'enabled': True
    }
    config_filepath = 'config.json'
    config = load_config(config_filepath, defaults)
    print('Loaded configuration:', config)