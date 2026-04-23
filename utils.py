import time
import random
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"Attempt {attempt + 1} failed: {err}")
            if attempt < retries - 1:
                wait_time = delay * (2 ** attempt) + random.uniform(0, 1)
                print(f"Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
            else:
                raise NetworkError(f"Failed to retrieve data after {retries} attempts")
    return None
