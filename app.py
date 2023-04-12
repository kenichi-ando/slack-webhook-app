import request
import os
import json

def post_message(message: str) -> None:
    print(f"[POST] {message}\n")
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "text": f"{message}"
    }
    request.urlopen(request.Request(os.environ.get("WEBHOOK_URL"), json.dumps(data).encode(), headers))

post_message("Hello, World!")
