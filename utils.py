import time
import requests

def retry_request(url, max_retries=5, backoff_factor=0.3, timeout=5):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            retries += 1
            wait_time = backoff_factor * (2 ** (retries - 1))
            print(f"Retry {retries}/{max_retries} for {url} after error: {e}")
            time.sleep(wait_time)
    raise Exception(f"Max retries exceeded for {url}")

# Example usage:
# response = retry_request('https://api.example.com/data')