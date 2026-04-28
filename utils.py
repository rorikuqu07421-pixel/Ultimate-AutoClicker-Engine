import json

def read_config(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")
        return None


def write_config(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Config written to {file_path}.")
    except IOError:
        print(f"Error: Could not write to {file_path}.")


def update_config(file_path, updates):
    config = read_config(file_path)
    if config is not None:
        config.update(updates)
        write_config(file_path, config)


def display_config(file_path):
    config = read_config(file_path)
    if config is not None:
        print(json.dumps(config, indent=4))
