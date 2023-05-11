from .currencies import LegacyCurrency
from .enums import AppID

from typing import Any

import requests


class InvalidItemOrAppIDException(Exception):
    """Exception raised when an item or app ID, or the combination of the two, is considered to be invalid by the Steam Community Market.

    .. versionadded:: 1.3.0

    Parameters
    ----------
    app_id : int or AppID
        The app ID the item belongs to.
    market_hash_name : str
        The market hash name of the item.
    message_format : str
        The format of the exception message. Defaults to ``Item "{}" with app ID "{}" is considered invalid by the Steam Community Market.``.
    """

    def __init__(
        self,
        app_id: int or AppID,
        market_hash_name: str,
        message_format: str = 'Item "{}" with app ID "{}" is considered invalid by the Steam Community Market.',
    ) -> None:
        message = message_format.format(market_hash_name, app_id)
        super().__init__(message)


class InvalidLanguageException(Exception):
    """Exception raised when a language is considered to be invalid by the Steam Community Market.

    .. versionadded:: 1.3.0

    Parameters
    ----------
    language : Any
        The unsupported invalid language.
    message_format : str
        The format of the exception message. Defaults to ``Language "{}" is considered invalid by the Steam Community Market.``.
    """

    def __init__(
        self,
        language: Any,
        message_format: str = 'Language "{}" is considered invalid by the Steam Community Market.',
    ) -> None:
        message = message_format.format(language)
        super().__init__(message)


class InvalidCurrencyException(Exception):
    """Exception raised when a currency is considered to be invalid by the Steam Community Market.

    .. versionadded:: 1.3.0

    Parameters
    ----------
    currency : Any
        The unsupported invalid currency.
    message_format : str
        The format of the exception message. Defaults to ``Currency "{}" is considered invalid by the Steam Community Market.``.
    """

    def __init__(
        self,
        currency: Any,
        message_format: str = 'Currency "{}" is considered invalid by the Steam Community Market.',
    ) -> None:
        message = message_format.format(currency)
        super().__init__(message)


class LegacyCurrencyException(Exception):
    """Exception raised when a currency is not supported by the Steam Community Market anymore.

    .. versionadded:: 1.3.0

    Parameters
    ----------
    currency : LegacyCurrency
        The unsupported legacy currency.
    message_format : str
        The format of the exception message. Defaults to ``Currency "{}" is not supported by the Steam Community Market anymore.``.
    """

    def __init__(
        self,
        currency: LegacyCurrency,
        message_format: str = 'Currency "{}" is not supported by the Steam Community Market anymore.',
    ) -> None:
        message = message_format.format(currency.name)
        super().__init__(message)


class TooManyRequestsException(requests.exceptions.RequestException):
    """Exception raised when too many requests are sent to the Steam Community Market.

    .. versionadded:: 1.3.0

    Parameters
    ----------
    message : str
        The exception message. Defaults to ``Too many requests have been sent to the Steam Community Market.``.
    """

    def __init__(
        self,
        message: str = "Too many requests have been sent to the Steam Community Market.",
    ) -> None:
        super().__init__(message)
