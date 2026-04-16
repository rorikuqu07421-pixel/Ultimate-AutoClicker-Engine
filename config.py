import json
import os

def load_config(filename='config.json', defaults=None):
    if defaults is None:
        defaults = {}
    if not os.path.isfile(filename):
        return defaults
    with open(filename, 'r') as file:
        try:
            config = json.load(file)
        except json.JSONDecodeError:
            return defaults
    return {**defaults, **config}

if __name__ == '__main__':
    default_config = {
        'click_interval': 0.1,
        'click_count': 100,
        'mouse_button': 'left'
    }
    config = load_config(defaults=default_config)
    print(config)