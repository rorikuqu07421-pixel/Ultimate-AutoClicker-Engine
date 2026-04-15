import json
import os

def save_click_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def load_click_data(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} does not exist.")
    with open(filename, 'r') as file:
        return json.load(file)


def filter_clicks_by_time(data, start_time, end_time):
    return [click for click in data if start_time <= click['timestamp'] <= end_time]


def format_click_data(data):
    return [f"{click['timestamp']}: Clicked at position {click['position']}" for click in data]


def aggregate_clicks(data):
    positions = {}
    for click in data:
        pos = click['position']
        if pos in positions:
            positions[pos] += 1
        else:
            positions[pos] = 1
    return positions
