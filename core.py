import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, method='GET', retries=3, delay=2, params=None):
    attempts = 0
    while attempts < retries:
        try:
            if method.upper() == 'GET':
                response = requests.get(url, params=params)
            elif method.upper() == 'POST':
                response = requests.post(url, json=params)
            else:
                raise ValueError('Unsupported method: {}'.format(method))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f'HTTP error: {e}')
            attempts += 1
            time.sleep(delay)
        except requests.exceptions.RequestException as e:
            print(f'Network error: {e}')
            attempts += 1
            time.sleep(delay)
    raise NetworkError(f'Failed to connect after {retries} attempts')

# Example of usage
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url, retries=5)
        print(data)
    except NetworkError as e:
        print(e)