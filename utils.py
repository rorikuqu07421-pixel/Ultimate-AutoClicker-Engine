import time
import requests

class NetworkError(Exception):
    pass

def retry_decorator(retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (requests.ConnectionError, requests.Timeout) as e:
                    if attempt < retries - 1:
                        time.sleep(delay)
                    else:
                        raise NetworkError(f"Network operation failed after {retries} attempts: {e}")
        return wrapper
    return decorator

@retry_decorator(retries=5, delay=1)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()