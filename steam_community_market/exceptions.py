from .currencies import SteamLegacyCurrency
from .enums import AppID

from typing import Any

import requests


class InvalidItemOrAppIDException(Exception):
    """Exception raised when an item or app ID, or the combination of the two, is considered to be invalid by the Steam Community Market.

    This exception class is used to handle cases where a given item or app ID, or the combination of the two, is not
    supported by the Steam Community Market.

    Attributes:
        app_id (int or AppID): The app ID.
        market_hash_name (str): The market hash name.
        message_format (str): The format of the exception message.

    :param app_id: The app ID.
    :type app_id: int or AppID
    :param market_hash_name: The market hash name.
    :type market_hash_name: str
    :param message_format: The format of the exception message.
    :type message_format: str
    :value message_format: 'Item "{}" with app ID "{}" is considered invalid by the Steam Community Market.'

    .. versionadded:: 1.3.0
    """

    def __init__(
        self,
        app_id: int or AppID,
        market_hash_name: str,
        message_format: str = 'Item "{}" with app ID "{}" is considered invalid by the Steam Community Market.',
    ) -> None:
        """Initialize the InvalidItemOrAppIDException with the app ID and market hash name.

        :param app_id: The app ID.
        :type app_id: int or AppID
        :param market_hash_name: The market hash name.
        :type market_hash_name: str
        :param message_format: The format of the exception message.
        :type message_format: str
        :value message_format: 'Item "{}" with app ID "{}" is considered invalid by the Steam Community Market.'
        """

        message = message_format.format(market_hash_name, app_id)
        super().__init__(message)


class InvalidCurrencyException(Exception):
    """Exception raised when a currency is considered to be invalid by the Steam Community Market.

    This exception class is used to handle cases where a given currency is not
    supported by the Steam Community Market.

    Attributes:
        currency (Any): The unsupported invalid currency.
        message_format (str): The format of the exception message.

    :param currency: The unsupported invalid currency.
    :type currency: Any
    :param message_format: The format of the exception message.
    :type message_format: str
    :value message_format: 'Currency "{}" is considered invalid by the Steam Community Market.'

    .. versionadded:: 1.3.0
    """

    def __init__(
        self,
        currency: Any,
        message_format: str = 'Currency "{}" is considered invalid by the Steam Community Market.',
    ) -> None:
        """Initialize the InvalidCurrencyException with the unsupported invalid currency.

        :param currency: The unsupported invalid currency.
        :type currency: Any
        :param message_format: The format of the exception message.
        :type message_format: str
        :value message_format: 'Currency "{}" is considered invalid by the Steam Community Market.'
        """

        message = message_format.format(currency)
        super().__init__(message)


class LegacyCurrencyException(Exception):
    """Exception raised when a currency is not supported by the Steam Community Market anymore.

    This exception class is used to handle cases where a given currency was previously
    supported but is no longer supported by the Steam Community Market.

    Attributes:
        currency (SteamLegacyCurrency): The unsupported legacy currency.
        message_format (str): The format of the exception message.

    :param currency: The unsupported legacy currency.
    :type currency: SteamLegacyCurrency
    :param message_format: The format of the exception message.
    :type message_format: str
    :value message_format: 'Currency "{}" is not supported by the Steam Community Market anymore.'

    .. versionadded:: 1.3.0
    """

    def __init__(
        self,
        currency: SteamLegacyCurrency,
        message_format: str = 'Currency "{}" is not supported by the Steam Community Market anymore.',
    ) -> None:
        """Initialize the LegacyCurrencyException with the unsupported legacy currency.

        :param currency: The unsupported legacy currency.
        :type currency: SteamLegacyCurrency
        :param message_format: The format of the exception message.
        :type message_format: str
        :value message_format: 'Currency "{}" is not supported by the Steam Community Market anymore.'
        """
        message = message_format.format(currency.name)
        super().__init__(message)


class TooManyRequestsException(requests.exceptions.RequestException):
    """Exception raised when too many requests are sent to the Steam Community Market.

    This exception class is used to handle cases where too many requests are sent to the Steam Community Market.

    Attributes:
        message (str): The exception message.

    :param message: The exception message.
    :type message_format: str
    :value message_format: 'Too many requests have been sent to the Steam Community Market.'

    .. versionadded:: 1.3.0
    """

    def __init__(
        self,
        message: str = "Too many requests have been sent to the Steam Community Market.",
    ) -> None:
        """Initialize the TooManyRequestsException.

        :param message: The exception message.
        :type message: str
        :value message: 'Too many requests have been sent to the Steam Community Market.'
        """

        super().__init__(message)
