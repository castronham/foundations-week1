import json
import requests

# A correct, working API URL
URL = "https://jsonplaceholder.typicode.com/users"

# UNCOMMENT the line below later if you want to test a broken 404 URL link!
# URL = "https://jsonplaceholder.typicode.com/broken-link-test"

print("Connecting to live server and checking HTTP status protocols...")

try:
    response = requests.get(URL, timeout=10)
    
    # Check the HTTP Status Code sent by the server
    status_code = response.status_code
    print(f"Server Response Code: {status_code}")
    
    # If the status code is not in the 200 success range, raise an error automatically
    response.raise_for_status()
    
    # If we pass the check, process the JSON data safely
    users = response.json()
    
    biz_email_count = 0
    company_names = []
    
    for user in users:
        email = user['email']
        company_name = user['company']['name']
        if email.endswith(".biz"):
            biz_email_count = biz_email_count + 1
        company_names.append(company_name)

    print("\n--- LIVE DATA API ANALYZER (FINAL) ---")
    print(f"Profiles Evaluated: {len(users)}")
    print(f"Profiles using '.biz' Emails: {biz_email_count}")

except requests.exceptions.HTTPError as http_err:
    print(f"\n[HTTP Error Detected]: The server responded with a failure status code: {response.status_code}")
except requests.exceptions.ConnectionError:
    print("\n[Network Error]: Could not reach the server. Please check your internet connection.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")