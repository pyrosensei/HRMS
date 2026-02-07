import requests
import json
import sys

def test_add_employee():
    url = "http://localhost:8000/employees/"
    payload = {
        "name": "Test User",
        "email": "test.user@example.com",
        "department": "Engineering"
    }
    headers = {
        "Content-Type": "application/json"
    }

    print(f"Attempting to add employee to {url}...")
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")

        if response.status_code == 200:
            print("SUCCESS: Employee added.")
            return True
        elif response.status_code == 400 and "Email already registered" in response.text:
            print("SUCCESS (Technically): API reachable, caught duplicate email.")
            return True
        else:
            print("FAILURE: Could not add employee.")
            return False

    except requests.exceptions.ConnectionError:
        print("ERROR: Connection failed. Is the server running?")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    if not test_add_employee():
        sys.exit(1)
