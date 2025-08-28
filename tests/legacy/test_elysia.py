# Legacy integration-style test moved to tests/legacy for reference
# This test was previously at repository root and may rely on a running server.
# It is kept for manual/local runs and is not part of CI.

import time

import requests

base_url = "http://localhost:8000"


def wait_for_server(timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(base_url + "/health", timeout=2)
            if r.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(1)
    return False


if __name__ == "__main__":
    if not wait_for_server():
        print("Server not available")
        exit(1)
    print("Server ready. Running manual legacy tests...")
    # ...manual interactions
