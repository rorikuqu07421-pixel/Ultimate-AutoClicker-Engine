import json
import os

def load_config(config_path, default_config):
    if not os.path.exists(config_path):
        return default_config
    with open(config_path, 'r') as file:
        return {**default_config, **json.load(file)}

if __name__ == '__main__':
    default_settings = {
        'click_interval': 0.1,
        'duration': 60,
        'click_type': 'left'
    }
    config = load_config('config.json', default_settings)
    print('Loaded Configuration:', config)