from steam_community_market.request import request
from typing import Union
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


class Market:
    url = 'http://steamcommunity.com/market/priceoverview'

    def __init__(self, currency: (str, int) = 1):
        """
        Sets the currency to be outputted.
        :param currency: 1, 'USD' or leave empty for American Dollars. For other currencies take a look at the README.
        """

        if isinstance(currency, str):
            currency = currency.upper()

            if currency in [i.name for i in ESteamCurrency]:
                currency = ESteamCurrency[currency].value

        if isinstance(currency, int):
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

        if self.has_invalid_name(name):
            name = self.fix_name(name)

        payload = {'appid': app_id, 'market_hash_name': name,
                   'currency': self.currency}

        return request(self.url, payload)

    def get_prices(self, names: list, app_id: (int, list)) -> dict:
        """
        Gets the price(s) and volume of each item in the list. If both are lists, then they need to have the same amount of elements.
        :param names: A list of item names how each item appears on the Steam Community Market.
        :param app_id: The AppID of the item(s). Either a list or int. For more information check the example.py file.
        """

        prices = {}

        if not isinstance(names, list):
            raise TypeError('names must be list')
        
        if isinstance(app_id, int):
            for name in names:
                prices[name] = self.get_price(name, app_id)

        elif isinstance(app_id, list):
            if len(names) == len(app_id):
                for i in range(len(names)):
                    name = names[i]
                    prices[name] = self.get_price(name, app_id[i])
            else:
                raise IndexError('names and app_id needs to have the same len')

        return prices

    def get_prices_from_dict(self, items: dict) -> dict:
        """
        Gets the price(s) and volume of each item in the list. 
        :param items: A dict including item names and AppIDs. Check example.py file for more information.
        """

        prices = {}

        if not isinstance(items, dict):
            raise TypeError('items must be dict')

        for item in items:
            prices[item] = self.get_price(item, items[item]['appid'])
        return prices

    def has_invalid_name(self, name: str) -> bool:
        if isinstance(name, str):
            try:
                return name.index('/') >= 0
            except ValueError:
                return False
        return False

    def fix_name(self, name: str):
        if isinstance(name, str):
            return name.replace('/', '-')
        return False
