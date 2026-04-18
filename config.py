import json
import os

def load_config(defaults_path, user_path):
    if not os.path.exists(user_path):
        return load_defaults(defaults_path)
    return load_user_config(user_path)


def load_defaults(path):
    with open(path, 'r') as f:
        return json.load(f)


def load_user_config(path):
    with open(path, 'r') as f:
        user_config = json.load(f)
        defaults = load_defaults('defaults.json')
        return {**defaults, **user_config}


if __name__ == '__main__':
    print(load_config('defaults.json', 'user_config.json'))