import os
import json

class Config:
    def __init__(self, config_file='settings.json'):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f'Config file {self.config_file} not found.')
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def save(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def update(self, key, value):
        self.settings[key] = value
        self.save()