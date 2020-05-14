import requests
import json


def request(url: str, payload: dict) -> dict:
    r = requests.get(url, payload)

    try:
        return json.loads(r.text)
    except ValueError:
        return {"success": False, "status_code": r.status_code, "text": r.text}
