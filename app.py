from urllib import request
import os
import json
import time

def post_message(message: str) -> None:
    print(f"[POST] {message}\n")
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "text": f"{message}"
    }
    request.urlopen(request.Request(os.environ.get("WEBHOOK_URL"), json.dumps(data).encode(), headers))

for i in range(5):
    post_message(f"Hello, World! {i + 1}")
    time.sleep(3)
