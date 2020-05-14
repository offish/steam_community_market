from steam_community_market.enums import ESteamCurrency, AppID
from steam_community_market.request import request


# These currencies will not be returned as float, but str instead due to weird formatting
UNSUPPORTED_CURRENCY = [
    "RUB",
    "VND",
    "KRW",
    "CLP",
    "PEN",
    "COP",
    "CRC"
]


class Market:
    URI = "http://steamcommunity.com/market/priceoverview"

    def __init__(self, currency = ESteamCurrency.USD):
        """Sets the currency to be outputted.

        :param currency: Currency used for prices. 
        :type currency: :class:`ESteamCurrency`, :class:`int`, :class:`str`
        """

        if isinstance(currency, ESteamCurrency):
            self.currency = currency.value

        elif isinstance(currency, str):
            self.currency = ESteamCurrency[currency.upper()].value

        elif isinstance(currency, int):
            self.currency = ESteamCurrency(currency).value

        else:
            self.currency = 1


    def get_overview(self, name: str, app_id) -> dict:
        """
        Gets the prices and volume of an item.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :param app_id: The AppID of the game the item is from.
        :type app_id: :class:`int`, :class:`AppID`
        :return: An overview of the item on success, :class:`None` otherwise. Overview includes both volume and prices.
        :rtype: Optional[:class:`dict`]

        .. versionchanged:: 1.2.2
        .. versionadded:: 1.0.0
        """

        if not isinstance(name, str):
            raise TypeError(f"name must be str not {type(name)}")
        
        if isinstance(app_id, AppID):
            app_id = app_id.value
        
        elif isinstance(app_id, int):
            app_id = app_id
        
        else:
            raise TypeError(f"app_id must be int or AppID not {type(app_id)}")
        
        if self.has_invalid_name(name):
            name = self.fix_name(name)

        payload = {"appid": app_id, "market_hash_name": name, "currency": self.currency}
        response = request(self.URI, payload)

        if response["success"] == True:
            return response
        return None


    def get_overviews(self, names: list, app_id) -> dict:
        """
        Gets the overview of each item in the list.
        
        :param names: A list of item names how they appear on the Steam Community Market.
        :type names: :class:`list`
        :param app_id: If given a list, it needs to have the same length as the `names`. \
            If given :class:`int` or :class:`AppID`, every item in `names` must have this AppID.
        :type app_id: :class:`list`, :class:`int`, :class:`AppID`
        :return: An overview of each item. 
        :rtype: :class:`dict`

        .. versionchanged:: 1.2.0
        .. versionadded:: 1.0.0
        """

        prices = {}

        if isinstance(app_id, AppID):
            app_id = app_id.value
        
        if isinstance(app_id, int):
            for name in names:
                prices[name] = self.get_overview(name, app_id)
        
        elif isinstance(app_id, list):
            if len(names) == len(app_id):
                for i in range(len(names)):
                    name = names[i]
                    prices[name] = self.get_overview(name, app_id[i])
            else:
                raise IndexError("names and app_id must have the same length")
        
        else:
            raise TypeError(f"app_id must be int, AppID or list not {type(app_id)}")
        
        return prices


    def get_volume(self, name: str, app_id):
        """
        Gets the volume of an item.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :param app_id: The AppID of the game the item is from.
        :type app_id: :class:`int`, :class:`ESteamCurrency`
        :return: The volume if success, :class:`None` otherwise.
        :rtype: Optional[:class:`int`]

        .. versionadded:: 1.2.0
        """

        item = self.get_overview(name, app_id)

        if item == None:
            return None
  
        if "volume" in item:
            return int(item["volume"].replace(",", ""))
        return None


    def get_prices(self, name: str, app_id):
        """
        Gets the lowest and/or median price of an item, if they exist.
        
        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :param app_id: The AppID of the game the item is from.
        :type app_id: :class:`int`, :class:`ESteamCurrency`
        :return: The lowest and/or median price of the item, if suceess. :class: `None` otherwise.
        :rtype: Optional[:class:`dict`]

        .. versionadded:: 1.2.0
        """

        item = self.get_overview(name, app_id)
        prices = {}

        if item == None:
            return None

        if "lowest_price" in item:
            prices["lowest_price"] = self.price_to_float(item["lowest_price"])

        if "median_price" in item:
            prices["median_price"] = self.price_to_float(item["median_price"])
        
        if len(prices) > 0:
            return prices
        return None


    def get_lowest_price(self, name: str, app_id):
        """
        Gets the lowest price of an item.
        
        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :param app_id: The AppID of the game the item is from.
        :type app_id: :class:`int`, :class:`ESteamCurrency`
        :return: The lowest price of the item, if suceess. :class: `None` otherwise.
        :rtype: Optional[Union[:class:`float`, :class:`str`]]

        .. versionadded:: 1.2.0  
        """

        item = self.get_overview(name, app_id)

        if item == None:
            return None

        if "lowest_price" in item:
            return self.price_to_float(item["lowest_price"])
        return None


    def get_median_price(self, name: str, app_id):
        """
        Gets the median price of an item.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :param app_id: The AppID of the game the item is from.
        :type app_id: :class:`int`, :class:`ESteamCurrency`
        :return: The median price of the item, if suceess. :class: `None` otherwise.
        :rtype: Optional[Union[:class:`float`, :class:`str`]]

        .. versionadded:: 1.2.0
        """
        item = self.get_overview(name, app_id)

        if item == None:
            return None

        if "median_price" in item:
            return self.price_to_float(item["median_price"])
        return None


    def get_overviews_from_dict(self, items: dict) -> dict:
        """
        Gets the overview of each item in the :class:`dict`.
        
        :param items: A :class:`dict` containg item names and AppIDs. There is an \
            example on how this :class:`dict` should be constructed in ``example.py``.
        :type items: :class:`dict`
        :return: An overview of each item.
        :rtype: :class:`dict`

        .. versionadded:: 1.1.0
        """

        prices = {}

        if not isinstance(items, dict):
            raise TypeError(f"items must be dict not {type(items)}")

        for item in items:
            prices[item] = self.get_overview(item, items[item]["appid"])
        return prices


    def price_to_float(self, value: str):
        """
        Converts a price from :class:`str` to :class:`float`

        :param value: A price
        :type value: :class:`str`
        :return: :class:`float` if currency is not in :class:`UNSUPPORTED_CURRENCY`
        :rtype: Optional[Union[:class:`float`, :class:`str`]]
        """
        
        if ESteamCurrency(self.currency).name in UNSUPPORTED_CURRENCY:
            return value

        price = ""

        for char in value.replace(",", "."):
            if char.isnumeric() or char == ".":
                price += char

        try:
            return float(price)
        except ValueError:
            return value

    def has_invalid_name(self, name: str) -> bool:
        """
        Checks if given item name is invalid.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :return: :class:`True` if the item name is invalid, :class:`False` otherwise.
        :rtype: :class:`bool`

        .. versionadded 1.1.0
        """
        
        if isinstance(name, str):
            try:
                return name.index("/") >= 0
            except ValueError:
                return False
        raise TypeError(f"name must be str not {type(name)}")


    def fix_name(self, name: str) -> str:
        """
        Replaces "/" with "-" and returns the item name.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :return: The correct item name.
        :rtype: :class:`str`

        .. versionadded 1.1.0
        """

        if isinstance(name, str):
            return name.replace("/", "-")
        raise TypeError(f"name must be str not {type(name)}")
