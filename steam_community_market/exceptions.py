from steam_community_market.enums import ESteamUnsupportedCurrency


class SteamUnsupportedCurrency(Exception):
    def __init__(self, currency: ESteamUnsupportedCurrency) -> None:
        self.currency = currency

    def __str__(self) -> str:
        return f'Currency "{self.currency.name}" is not supported by the Steam Community Market anymore.'
