import json

def load_config(file_path):
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f'Config file not found: {file_path}')
    except json.JSONDecodeError:
        raise ValueError('Error decoding JSON from the config file')


def save_config(file_path, config_data):
    with open(file_path, 'w') as file:
        json.dump(config_data, file, indent=4)


def merge_configs(defaults, custom):
    merged = defaults.copy()
    merged.update(custom)
    return merged


def validate_click_data(data):
    required_keys = ['click_interval', 'click_count', 'target']
    for key in required_keys:
        if key not in data:
            raise KeyError(f'Missing required key: {key}')
        if not isinstance(data[key], (int, float)):
            raise TypeError(f'Key {key} must be an integer or float')
    return True


def format_click_data(data):
    return f"Clicking {data['click_count']} times at {data['click_interval']}ms interval on {data['target']}"