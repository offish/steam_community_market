import requests


def request(url: str, payload: dict) -> dict:
    """Make a request to the Steam Community Market API.

    :param url: The URL of the API endpoint.
    :type url: str
    :param payload: The payload to send with the request.
    :type payload: dict
    :return: The response from the API endpoint.
    :rtype: dict
    """
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
