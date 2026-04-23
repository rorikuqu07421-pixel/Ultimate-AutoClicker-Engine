import json
import os

def load_config(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Configuration file not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)


def save_config(config, file_path):
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)


def update_config(config, updates):
    config.update(updates)
    return config


def validate_config(config):
    required_keys = ['click_interval', 'max_clicks', 'enabled']
    for key in required_keys:
        if key not in config:
            raise ValueError(f'Missing required config key: {key}')  
    if not isinstance(config['click_interval'], (int, float)) or config['click_interval'] <= 0:
        raise ValueError('click_interval must be a positive number')
    if not isinstance(config['max_clicks'], int) or config['max_clicks'] < 0:
        raise ValueError('max_clicks must be a non-negative integer')
    if not isinstance(config['enabled'], bool):
        raise ValueError('enabled must be a boolean value')

    return True
