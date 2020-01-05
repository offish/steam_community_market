from steam_community_market.request import request
import enum


class ESteamCurrency(enum.IntEnum):
    USD = 1
    GBP = 2
    EUR = 3
    CHF = 4
    RUB = 5
    PLN = 6
    BRL = 7
    JPY = 8
    NOK = 9
    IDR = 10
    MYR = 11
    PHP = 12
    SGD = 13
    THB = 14
    VND = 15
    KRW = 16
    TRY = 17
    UAH = 18
    MXN = 19
    CAD = 20
    AUD = 21
    NZD = 22
    CNY = 23
    INR = 24
    CLP = 25
    PEN = 26
    COP = 27
    ZAR = 28
    HKD = 29
    TWD = 30
    SAR = 31
    AED = 32


class Prices:
    url = 'http://steamcommunity.com/market/priceoverview'

    def __init__(self, currency: (str, int) = 1):
        """
        Sets the currency to be outputted.

        :param currency: 1, 'USD' or leave empty for American Dollars. For other currencies take a look at the README.
        """

        if isinstance(currency, str):
            currency = currency.upper()

            for i in ESteamCurrency:
                if currency == i.name:
                    currency = ESteamCurrency[currency].value

        elif isinstance(currency, int):
            if currency > 32 or currency < 1:
                currency = 1

        else:
            currency = 1

        self.currency = currency

    def get_price(self, name: str, app_id: int) -> dict:
        """
        Gets the price(s) and volume of an item.
        :param name: The name of the item how it appears on the Steam Community Market.
        :param app_id: The AppID of the item.
        """

        if not isinstance(name, str):
            raise TypeError('name must be str')

        if not isinstance(app_id, int):
            raise TypeError('app_id must be int')

        payload = {'appid': app_id, 'market_hash_name': name,
                   'currency': self.currency}

        return request(self.url, payload)

    def get_prices(self, names: list, app_id: int) -> dict:
        """
        Gets the price(s) and volume of each item in the list.

        :param names: A list of item names how each item appears on the Steam Community Market.
        :param app_id: The AppID of all the items. Every item in the list must have the same AppID.
        """

        prices = {}

        if not isinstance(names, list):
            raise TypeError('names must be list')

        for name in names:
            prices[name] = self.get_price(name, app_id)
        return prices
