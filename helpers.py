import time
import random
import requests

class NetworkError(Exception):
    pass

def retry(network_operation, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return network_operation()
        except (requests.ConnectionError, requests.Timeout) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay * (2 ** attempt) + random.uniform(0, 1))  # Exponential backoff with jitter
            else:
                raise NetworkError(f'Operation failed after {retries} attempts')

# Example network operation function

def fetch_data():
    # Simulating a network request with a potential for failure
dummy_response = ["Data fetched successfully", "Network error"]
    result = random.choice(dummy_response)
    if result == "Network error":
        raise requests.ConnectionError("Simulated connection error")
    return result

# Usage Example
if __name__ == '__main__':
    try:
        print(retry(fetch_data))
    except NetworkError as ne:
        print(ne)