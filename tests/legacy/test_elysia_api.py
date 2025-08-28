# Legacy API test harness moved to tests/legacy for manual use
# This uses requests and expects a running server at localhost:8000
import json

import requests

base_url = "http://localhost:8000"

if __name__ == "__main__":
    print("Running legacy API harness...")
    r = requests.get(base_url + "/")
    print(r.status_code, r.text)
    r = requests.get(base_url + "/health")
    print(r.status_code, r.text)
