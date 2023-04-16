from .enums import AppID
from .currencies import SteamCurrency
from .exceptions import InvalidItemOrAppIDException, TooManyRequestsException

from typing import Union

import contextlib
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


def _request(url: str, payload: dict) -> tuple[int, dict]:
    """Make a request to the Steam Community Market API.

    :param url: The URL of the API endpoint.
    :type url: str
    :param payload: The payload to send with the request.
    :type payload: dict
    :return: The status code and response data as a :obj:`tuple`.
    :rtype: tuple[int, dict]

    .. versionchanged:: 1.3.0
    """

    response = requests.get(url, params=payload, headers=REQUEST_HEADERS)
    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Check if the status code is 429 (Too Many Requests) and raise a "TooManyRequestsException".
        if response.status_code == 429:
            raise TooManyRequestsException from e

    data = None
    with contextlib.suppress(ValueError):
        data = response.json()

    return (response.status_code, data)


def _request_overview(
    app_id: int,
    market_hash_name: str,
    currency: SteamCurrency,
    raise_exception: bool = True,
) -> dict[str, Union[bool, str]]:
    """Make a request to the Steam Community Market API to get an overview of a
    specific item.

    :param app_id: The ID of the game.
    :type app_id: int
    :param market_hash_name: The market hash name of the item.
    :type market_hash_name: str
    :return: The response data as a :obj:`dict`.
    :rtype: dict[str, bool or str]

    .. versionadded:: 1.3.0
    """

    url = "https://steamcommunity.com/market/priceoverview/"

    payload = {
        "appid": _app_id_value(app_id),
        "market_hash_name": _fix_item_name(market_hash_name),
        "currency": currency.value,
    }

    status_code, data = _request(url, payload)
    # 500 - Internal Server Error
    if raise_exception and status_code == 500 and data["success"] is False:
        raise InvalidItemOrAppIDException(app_id, market_hash_name)

    return data


def _app_id_value(app_id: Union[int, list[Union[int, AppID]], AppID]) -> int:
    """Validates and returns the value/s of the :class:`AppID`/s.

    .. currentmodule:: steam_community_market.enums

    :param app_id: The :class:`AppID` of the game.
    :type app_id: int or list[int or AppID] or AppID
    :return: The value of the :class:`AppID`.
    :rtype: int
    :raises TypeError: Raised when the ``app_id`` is not of a supported type.

    .. versionadded:: 1.3.0
    """

    if isinstance(app_id, AppID):
        return app_id.value

    if isinstance(app_id, int):
        return app_id

    raise TypeError(f'"app_id" must be "int" or "AppID", not "{type(app_id)}".')


def _fix_item_name(market_hash_name: str) -> str:
    """Replaces "/" with "-" and returns the item name.

    :param market_hash_name: The name of the item how it appears on the Steam Community Market.
    :type market_hash_name: str
    :raises TypeError: If the given ``market_hash_name`` is not a string.
    :return: The correct item name.
    :rtype: str

    .. versionchanged:: 1.3.0
    .. versionadded:: 1.1.0
    """

    if isinstance(market_hash_name, str):
        return market_hash_name.replace("/", "-")

    raise TypeError(f'"name" must be "str", not "{type(market_hash_name)}".')
