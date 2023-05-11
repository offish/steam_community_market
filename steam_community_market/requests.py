from .currencies import Currency
from .exceptions import InvalidItemOrAppIDException, TooManyRequestsException

from typing import Callable, Optional, Union

import contextlib
import random
import requests
import time

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


def _market_request(
    endpoint: str,
    payload: dict,
    rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]],
) -> tuple[int, dict]:
    url = f"https://steamcommunity.com/market/{endpoint}/"

    retries = 0
    while True:
        status_code, data = _request(url, payload)
        if status_code != 429:
            break

        if rate_limit_handler is None:
            raise TooManyRequestsException

        retry, sleep_time = rate_limit_handler(retries)
        if not retry:
            break

        time.sleep(sleep_time)
        retries += 1

    return (status_code, data)


def _request(url: str, payload: dict) -> tuple[int, dict]:
    response = requests.get(url, params=payload, headers=REQUEST_HEADERS)

    data = None
    with contextlib.suppress(ValueError):
        data = response.json()

    return (response.status_code, data)


def _request_overview(
    app_id: int,
    market_hash_name: str,
    currency: Currency,
    raise_exception: bool = True,
    rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
) -> dict[str, Union[bool, str]]:
    payload = {
        "appid": app_id,
        "market_hash_name": market_hash_name,
        "currency": currency.value,
    }

    status_code, data = _market_request("priceoverview", payload, rate_limit_handler)
    # 500 - Internal Server Error
    if raise_exception and status_code == 500 and data["success"] is False:
        raise InvalidItemOrAppIDException(app_id, market_hash_name)

    return data


def exponential_backoff_strategy(
    retries: int, max_retries: int = 5
) -> tuple[bool, float]:
    """Default rate limit handler for the Steam Community Market API.

    .. versionadded:: 1.3.0

    Parameters
    ----------
    retries : int
        The number of retries that have been attempted.
    max_retries : int
        The maximum number of retries to attempt. Defaults to 5.

    Returns
    -------
    tuple[bool, float]
        A tuple containing a boolean indicating whether the request should be retried and the number of seconds to sleep for.
    """
    if retries >= max_retries:
        return (False, 0)

    # Exponential backoff with a random jitter
    return (True, ((2**retries) + random.uniform(0, 1)) * 60)
