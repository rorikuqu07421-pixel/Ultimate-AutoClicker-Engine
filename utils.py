import json
import os

def load_clicker_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f\"Configuration file not found: {file_path}\")
    with open(file_path, 'r') as file:
        try:
            config = json.load(file)
            validate_config(config)
            return config
        except json.JSONDecodeError:
            raise ValueError(f\"Invalid JSON format in configuration file: {file_path}\")


def validate_config(config):
    required_keys = ['click_interval', 'click_duration', 'click_count']
    for key in required_keys:
        if key not in config:
            raise KeyError(f\"Missing required configuration key: {key}\")
    if not isinstance(config['click_interval'], (int, float)):
        raise TypeError('click_interval must be a number')
    if not isinstance(config['click_duration'], (int, float)):
        raise TypeError('click_duration must be a number')
    if not isinstance(config['click_count'], int):
        raise TypeError('click_count must be an integer')


def save_clicker_config(file_path, config):
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)
