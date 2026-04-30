import requests
import time
import json

def retry_request(url, max_retries=5, backoff_factor=1):
    tries = 0
    while tries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            tries += 1
            wait = backoff_factor * (2 ** (tries - 1))
            print(f"Attempt {tries} failed: {e}. Retrying in {wait} seconds...")
            time.sleep(wait)
    raise Exception(f'All {max_retries} attempts failed.')

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(json.dumps(data, indent=4))
    except Exception as error:
        print(f'Error fetching data: {error}')