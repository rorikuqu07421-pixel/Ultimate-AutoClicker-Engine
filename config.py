import json
import os

def load_config(file_path='config.json', default_config=None):
    if default_config is None:
        default_config = {
            'click_rate': 100,
            'duration': 10,
            'max_clicks': 1000,
            'enabled': True
        }
    if not os.path.isfile(file_path):
        save_config(file_path, default_config)
        return default_config
    with open(file_path, 'r') as f:
        try:
            user_config = json.load(f)
            return {**default_config, **user_config}
        except json.JSONDecodeError:
            save_config(file_path, default_config)
            return default_config


def save_config(file_path, config):
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)
