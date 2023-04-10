from steam_community_market.currencies import SteamLegacyCurrency
from typing import Any


class InvalidCurrencyException(Exception):
    """Exception raised when a currency is considered to be invalid by the Steam Community Market.

    This exception class is used to handle cases where a given currency is not
    supported by the Steam Community Market.

    .. versionadded:: 1.3.0

    Attributes:
        currency (Any): The unsupported invalid currency.

    :param currency: The unsupported invalid currency.
    :type currency: Any
    """

    def __init__(self, currency: Any) -> None:
        """Initialize the InvalidCurrencyException with the unsupported invalid currency.

        :param currency: The unsupported invalid currency.
        :type currency: Any
        """

        self.currency = currency

    def __str__(self) -> str:
        """Return a string representation of the exception.

        This method returns a string that indicates which currency is not supported
        by the Steam Community Market.

        :return: A string representation of the exception.
        :rtype: str
        """

        return f'Currency "{self.currency}" is not supported by the Steam Community Market.'


class LegacyCurrencyException(Exception):
    """Exception raised when a currency is not supported by the Steam Community Market anymore.

    This exception class is used to handle cases where a given currency was previously
    supported but is no longer supported by the Steam Community Market.

    .. versionadded:: 1.3.0

    Attributes:
        currency (SteamLegacyCurrency): The unsupported legacy currency.

    :param currency: The unsupported legacy currency.
    :type currency: SteamLegacyCurrency
    """

    def __init__(self, currency: SteamLegacyCurrency) -> None:
        """Initialize the LegacyCurrencyException with the unsupported legacy currency.

        :param currency: The unsupported legacy currency.
        :type currency: SteamLegacyCurrency
        """

        self.currency = currency

    def __str__(self) -> str:
        """Return a string representation of the exception.

        This method returns a string that indicates which legacy currency is not supported
        by the Steam Community Market anymore.

        :return: A string representation of the exception.
        :rtype: str
        """

        return f'Currency "{self.currency.name}" is not supported by the Steam Community Market anymore.'
