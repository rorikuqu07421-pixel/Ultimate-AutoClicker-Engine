import time
import random

def retry_operation(func, retries=3, delay=2):
    attempt = 0
    while attempt < retries:
        try:
            return func()
        except Exception as e:
            attempt += 1
            if attempt == retries:
                print(f"Operation failed after {retries} attempts")
                raise e
            wait_time = delay + random.uniform(0, 1)
            print(f"Attempt {attempt} failed: {e}. Retrying in {wait_time:.2f} seconds...")
            time.sleep(wait_time)

# Example usage:
if __name__ == '__main__':
    def network_call():
        if random.choice([True, False]):  # Simulates network failure
            raise ConnectionError("Network issue")
        return "Success!"
    result = retry_operation(network_call)
    print(result)