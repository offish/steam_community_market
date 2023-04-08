import requests

#: Generic headers to send with each request to the Steam Community Market API.
REQUEST_HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "steamcommunity.com",
    "Referer": "https://steamcommunity.com/market/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "X-Requested-With": "XMLHttpRequest",
}


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
        response = requests.get(url, params=payload, headers=REQUEST_HEADERS)
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.RequestException, ValueError):
        return {
            "success": False,
            "status_code": response.status_code,
            "text": response.text,
        }
