import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=5, delay=2):
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            attempt += 1
            time.sleep(delay)
    raise Exception(f'Failed to retrieve data from {url} after {max_retries} attempts')

# Example use case
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except Exception as e:
        print(e)