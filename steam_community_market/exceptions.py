from steam_community_market.enums import ESteamUnsupportedCurrency


class SteamUnsupportedCurrency(Exception):
    """Exception raised when a currency is not supported by the Steam Community Market anymore.

    :param currency: The currency that is not supported by the Steam Community Market anymore.
    :type currency: ESteamUnsupportedCurrency
    """

    def __init__(self, currency: ESteamUnsupportedCurrency) -> None:
        """Raise an exception when a currency is not supported by the Steam Community Market anymore.

        :param currency: The currency that is not supported by the Steam Community Market anymore.
        :type currency: ESteamUnsupportedCurrency
        """

        self.currency = currency

    def __str__(self) -> str:
        """Return a string representation of the exception.

        :return: A string representation of the exception.
        :rtype: str
        """

        return f'Currency "{self.currency.name}" is not supported by the Steam Community Market anymore.'
