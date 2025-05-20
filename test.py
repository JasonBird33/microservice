import os
import time

IO_DIR = "io"
REQUEST_FILE = os.path.join(IO_DIR, "email-service.txt")
RESPONSE_FILE = os.path.join(IO_DIR, "email-response.txt")

def send_email_request(tracking_number, admin_email):
    os.makedirs(IO_DIR, exist_ok=True)

    # Clean up old files
    if os.path.exists(REQUEST_FILE):
        os.remove(REQUEST_FILE)
    if os.path.exists(RESPONSE_FILE):
        os.remove(RESPONSE_FILE)

    # Send request
    with open(REQUEST_FILE, "w") as f:
        f.write(f"{tracking_number}|{admin_email}")
    print(f"[Test] Sent request: {tracking_number}|{admin_email}")
    print("[Test] File created: email-service.txt file created, awaiting response from microservices...")

def wait_for_response(timeout=5):
    start = time.time()
    while not os.path.exists(RESPONSE_FILE):
        if time.time() - start > timeout:
            print("[Test] Timed out waiting for email microservice response.")
            return
        time.sleep(0.2)

    with open(RESPONSE_FILE, "r") as f:
        print(f"[Test] Microservice response: {f.read().strip()}")
    os.remove(RESPONSE_FILE)

if __name__ == "__main__":
    test_tracking = "TEST-001"
    test_email = "dole@oregonstate.edu"
    send_email_request(test_tracking, test_email)
    wait_for_response()
