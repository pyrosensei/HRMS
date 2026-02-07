import requests
import sys
import time

def check_server():
    url = "http://localhost:8000/"
    try:
        print(f"Checking {url}...")
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("Server is up and reachable!")
            print("Response content snippet:", response.text[:100])
            return True
        else:
            print(f"Server returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("Could not connect to server.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    success = check_server()
    if not success:
        sys.exit(1)
