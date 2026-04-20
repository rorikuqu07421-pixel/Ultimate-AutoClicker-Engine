import json
from typing import Any, Dict

def load_clicker_data(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            validate_clicker_data(data)
            return data
    except FileNotFoundError:
        raise Exception('File not found. Please check the path.')
    except json.JSONDecodeError:
        raise Exception('Error decoding JSON. Check file format.')


def validate_clicker_data(data: Dict[str, Any]) -> None:
    required_keys = ['click_interval', 'max_clicks', 'duration']
    for key in required_keys:
        if key not in data:
            raise Exception(f'Missing required key: {key}')
    if not isinstance(data['click_interval'], (int, float)):
        raise Exception('click_interval must be a number.')
    if not isinstance(data['max_clicks'], int) or data['max_clicks'] < 0:
        raise Exception('max_clicks must be a non-negative integer.')
    if not isinstance(data['duration'], (int, float)) or data['duration'] <= 0:
        raise Exception('duration must be a positive number.')


def save_clicker_data(file_path: str, data: Dict[str, Any]) -> None:
    validate_clicker_data(data)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
