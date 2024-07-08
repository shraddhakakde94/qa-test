import requests
import time

# Define the URL of the mock server
app_up_url = 'http://localhost:8000/up'
app_down_url = 'http://localhost:8000/down'

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True, f"Application is UP. Status Code: {response.status_code}"
        elif response.status_code == 503:
            return False, f"Application is DOWN. Status Code: {response.status_code}"
        else:
            return False, f"Unexpected response. Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Failed to connect to application. Error: {str(e)}"

if __name__ == "__main__":
    while True:
        # Check UP scenario
        is_up, status_message = check_application_health(app_up_url)
        print(status_message)

        if is_up:
            print("Application is functioning correctly. Taking normal monitoring actions.")
        else:
            print("Application is DOWN. Initiating recovery procedures.")

        # Wait for a specific interval before checking again (e.g., every 30 seconds)
        time.sleep(30)

        # Check DOWN scenario
        is_down, status_message = check_application_health(app_down_url)
        print(status_message)

        if is_down:
            print("Application is DOWN. Initiating recovery procedures.")
        else:
            print("Application is functioning correctly. Taking normal monitoring actions.")

        # Wait for a specific interval before checking again (e.g., every 30 seconds)
        time.sleep(30)
