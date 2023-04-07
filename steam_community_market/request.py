import requests


def request(url: str, payload: dict) -> dict:
    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.RequestException, ValueError):
        return {
            "success": False,
            "status_code": response.status_code,
            "text": response.text,
        }
