import os

class Config:
    def __init__(self):
        self.click_interval = 0.01  # seconds
        self.max_clicks = 10000
        self.output_directory = os.path.expanduser('~') + '/autoclicker'
        self.click_sound = True
        self.mouse_button = 'left'
        self.hotkey = 'ctrl+c'

    def update_settings(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f'Invalid config key: {key}')

    def display_settings(self):
        settings = {k: v for k, v in self.__dict__.items()}
        for key, value in settings.items():
            print(f'{key}: {value}')