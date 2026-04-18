import time
import random
import requests

def retry_network_operation(func, retries=3, delay=2, backoff=2):
    for attempt in range(retries):
        try:
            return func()
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                wait = delay * (backoff ** attempt)
                print(f'Attempt {attempt + 1} failed: {e}. Retrying in {wait} seconds...')
                time.sleep(wait)
            else:
                print('All attempts failed.')
                raise


def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# Example usage:
# data = retry_network_operation(lambda: fetch_data('https://api.example.com/data'))
