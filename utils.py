import time
import requests

class NetworkError(Exception):
    pass

def retry_network_operation(func, max_retries=5, delay=2, *args, **kwargs):
    attempts = 0
    while attempts < max_retries:
        try:
            return func(*args, **kwargs)
        except requests.RequestException as e:
            attempts += 1
            if attempts == max_retries:
                raise NetworkError(f'Network operation failed after {attempts} attempts: {e}')
            time.sleep(delay)
            delay *= 2  # Exponential backoff

# Example usage:
# response = retry_network_operation(requests.get, 'https://api.example.com/data')
