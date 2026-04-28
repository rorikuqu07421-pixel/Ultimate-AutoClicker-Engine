import time
import random
from validators import validate_click_params

def process_clicks(clicks_count, interval):
    for _ in range(clicks_count):
        validate_click_params(clicks_count, interval)
        perform_click()
        time.sleep(interval)


def perform_click():
    print("Click performed!")

if __name__ == '__main__':
    try:
        clicks = random.randint(1, 100)
        interval = random.uniform(0.1, 2.0)
        process_clicks(clicks, interval)
    except ValueError as e:
        print(f"Invalid input: {e}")