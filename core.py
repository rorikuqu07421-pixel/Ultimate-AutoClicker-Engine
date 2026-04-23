import json
import time
import random
from threading import Thread

class AutoClicker:
    def __init__(self, click_interval=0.1, duration=10):
        self.click_interval = click_interval
        self.duration = duration
        self.running = False

    def start(self):
        self.running = True
        click_thread = Thread(target=self.click)
        click_thread.start()

    def click(self):
        end_time = time.time() + self.duration
        while self.running and time.time() < end_time:
            self.perform_click()
            time.sleep(self.click_interval)

    def perform_click(self):
        click_position = (random.randint(0, 1920), random.randint(0, 1080))
        print(f"Clicking at {click_position}")  # Simulate a mouse click

    def stop(self):
        self.running = False

    def save_state(self, filename):
        state_data = {'click_interval': self.click_interval, 'duration': self.duration}
        with open(filename, 'w') as file:
            json.dump(state_data, file)

    @staticmethod
    def load_state(filename):
        with open(filename, 'r') as file:
            state_data = json.load(file)
        return state_data

if __name__ == '__main__':
    clicker = AutoClicker(0.5, 5)
    clicker.start()
    time.sleep(6)  # Let it click for 6 seconds
    clicker.stop()  
    clicker.save_state('clicker_state.json')  
    loaded_state = clicker.load_state('clicker_state.json')
    print(f"Loaded state: {loaded_state}")