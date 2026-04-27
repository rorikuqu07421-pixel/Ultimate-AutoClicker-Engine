import json
import os

def load_config(file_path):
    default_config = {
        'click_interval': 0.1,
        'clicks_per_session': 100,
        'randomize_clicks': True,
        'session_duration': 60
    }

    if not os.path.isfile(file_path):
        return default_config

    with open(file_path, 'r') as config_file:
        try:
            user_config = json.load(config_file)
            return {**default_config, **user_config}
        except json.JSONDecodeError:
            print("Error: Invalid JSON in config file, loading defaults.")
            return default_config

# Example usage:
if __name__ == '__main__':
    config = load_config('config.json')
    print(config)