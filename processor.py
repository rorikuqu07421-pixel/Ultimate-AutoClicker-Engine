import requests
import time
import json

class NetworkError(Exception):
    pass

class NetworkOperations:
    def __init__(self, max_retries=3, backoff_factor=1):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def _retry_request(self, url, method='GET', **kwargs):
        retries = 0
        while retries < self.max_retries:
            try:
                response = requests.request(method, url, **kwargs)
                response.raise_for_status()
                return response.json() if response.content else None
            except requests.RequestException as e:
                retries += 1
                if retries == self.max_retries:
                    raise NetworkError(f'Failed to fetch {url} after {retries} attempts')
                wait_time = self.backoff_factor * (2 ** (retries - 1))
                time.sleep(wait_time)
                print(f'Retrying {url}... (Attempt: {retries}) Error: {e}')  

    def fetch_data(self, url):
        return self._retry_request(url)

if __name__ == '__main__':
    network_ops = NetworkOperations()
    try:
        data = network_ops.fetch_data('https://api.example.com/data')
        print(json.dumps(data, indent=2))
    except NetworkError as e:
        print(e)