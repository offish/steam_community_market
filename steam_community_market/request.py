import requests
import json


def request(url: str, payload: dict) -> dict:
    r = requests.get(url, payload)

    if r.ok:
        return r.json()
    try:
        return json.loads(r.text)
    except ValueError:
        return {'success': False, 'code': r.status_code, 'reason': r.text}
