import requests
import time
import json

class NetworkOperationError(Exception):
    pass

def retry_request(url, retries=3, backoff=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                time.sleep(backoff ** attempt)
            else:
                raise NetworkOperationError(f'Failed to fetch data from {url}') from e

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(json.dumps(data, indent=4))
    except NetworkOperationError as e:
        print(e)