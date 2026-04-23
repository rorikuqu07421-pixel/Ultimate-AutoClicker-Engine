import time
import random
import requests

def retry_request(url, max_retries=5, wait_time=2):
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f'HTTP error occurred: {e}')
            attempt += 1
            time.sleep(wait_time)
        except requests.exceptions.RequestException as e:
            print(f'Network error occurred: {e}')
            return None
    print('Max retries exceeded')
    return None

if __name__ == '__main__':
    result = retry_request('https://api.example.com/data')
    if result:
        print('Data received:', result)
    else:
        print('Failed to retrieve data')