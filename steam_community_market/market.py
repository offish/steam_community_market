import re
from steam_community_market.enums import (
    AppID,
    ESteamCurrency,
    ESteamSupportedCurrency,
    ESteamUnsupportedCurrency,
)
from steam_community_market.exceptions import SteamUnsupportedCurrency
from steam_community_market.request import request


class Market:
    URI = "http://steamcommunity.com/market/priceoverview"

    def __init__(
        self, currency: int | str | ESteamCurrency = ESteamCurrency.USD
    ) -> None:
        """Sets the currency to be outputted.

        :param currency: Currency used for prices.
        :type currency: :class:`int`, :class:`str`, :class:`ESteamCurrency`
        """
        if isinstance(currency, ESteamUnsupportedCurrency):
            raise SteamUnsupportedCurrency(currency)

        self.currency = self._supported_currency(currency)

    @staticmethod
    def _supported_currency(
        currency: int | str | ESteamCurrency,
    ) -> ESteamSupportedCurrency:
        """
        Returns a supported currency.

        :param currency: Currency used for prices.
        :type currency: :class:`int`, :class:`str`, :class:`ESteamCurrency`
        :return: A supported currency.
        :rtype: :class:`ESteamSupportedCurrency`

        .. versionadded:: 1.2.4
        """

        if isinstance(currency, int):
            return ESteamSupportedCurrency(currency)
        if isinstance(currency, str):
            return ESteamSupportedCurrency[currency.upper()]
        if isinstance(currency, ESteamSupportedCurrency):
            return currency

        return ESteamSupportedCurrency.USD

    def get_overview(self, name: str, app_id: int | AppID) -> dict | None:
        """
        Gets the prices and volume of an item.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :param app_id: The AppID of the game the item is from.
        :type app_id: :class:`int`, :class:`AppID`
        :return: An overview of the item on success, :class:`None` otherwise. Overview includes both volume and prices.
        :rtype: :class:`dict`, :class:`None`

        .. versionchanged:: 1.2.4
        .. versionchanged:: 1.2.3
        .. versionadded:: 1.0.0
        """

        if not isinstance(name, str):
            raise TypeError(f'"name" must be "str", not "{type(name)}".')

        if self.has_invalid_name(name):
            name = self.fix_name(name)

        app_id = self._app_id_value(app_id)
        payload = {
            "appid": app_id,
            "market_hash_name": name,
            "currency": self.currency.value,
        }
        response = request(self.URI, payload)

        return None if not response or response["success"] == False else response

    def get_overviews(
        self, names: list[str], app_id: int | list[int, AppID] | AppID
    ) -> dict:
        """
        Gets the overview of each item in the list.
        
        :param names: A list of item names how they appear on the Steam Community Market.
        :type names: :class:`list[str]`
        :param app_id: If given a list, it needs to have the same length as the `names`. \
            If given :class:`int` or :class:`AppID`, every item in `names` must have this AppID.
        :type app_id: :class:`int`, :class:`list[int, AppID]`, :class:`AppID`
        :return: An overview of each item. 
        :rtype: :class:`dict`

        .. versionchanged:: 1.2.4
        .. versionchanged:: 1.2.0
        .. versionadded:: 1.0.0
        """

        prices = {}
        app_id = self._app_id_value(app_id, support_lists=True)
        if isinstance(app_id, list):
            if len(names) == len(app_id):
                prices = {
                    name: self.get_overview(name, id) for name, id in zip(names, app_id)
                }
            else:
                raise IndexError('"names" and "app_id" must have the same length.')

        else:
            prices = {name: self.get_overview(name, app_id) for name in names}

        return prices

    @staticmethod
    def _app_id_value(
        app_id: int | list[int | AppID] | AppID, support_lists: bool = False
    ) -> int:
        """
        Gets the value of the AppID.

        :param app_id: The AppID of the game the item is from.
        :type app_id: :class:`int`, list[int | AppID], :class:`AppID`
        :param support_lists: Whether or not to support lists.
        :type support_lists: :class:`bool`
        :return: The value of the AppID.
        :rtype: :class:`int`

        .. versionadded:: 1.2.4
        """

        if isinstance(app_id, AppID):
            return app_id.value
        if isinstance(app_id, int) or (
            support_lists and isinstance(app_id, list[int | AppID])
        ):
            return app_id

        raise TypeError(
            support_lists
            and f'"app_id" must be "int", "list" or "AppID", not "{type(app_id)}".'
            or f'"app_id" must be "int" or "AppID", not "{type(app_id)}".'
        )

    def get_overviews_from_dict(self, items: dict) -> dict:
        """
        Gets the overview of each item in the :class:`dict`.
        
        :param items: A :class:`dict` containg item names and AppIDs. There is an \
            example on how this :class:`dict` should be constructed in ``example.py``.
        :type items: :class:`dict`
        :return: An overview of each item.
        :rtype: :class:`dict`

        .. versionchanged:: 1.2.4
        .. versionadded:: 1.1.0
        """

        if not isinstance(items, dict):
            raise TypeError(f'"items" must be "dict", not "{type(items)}".')

        return {item: self.get_overview(item, items[item]["appid"]) for item in items}

    def get_prices(
        self, name: str, app_id: int | AppID
    ) -> dict[str, float | None] | None:
        """
        Gets the lowest and/or median price of an item, if they exist.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :param app_id: The AppID of the game the item is from.
        :type app_id: :class:`int`, :class:`AppID`
        :return: The lowest and/or median price of the item, if suceess. :class: `None` otherwise.
        :rtype: :class:`dict[str, float | None]`, :class:`None`

        .. versionchanged:: 1.2.4
        .. versionadded:: 1.2.0
        """

        item = self.get_overview(name, app_id)

        if item is None:
            return None

        prices: dict[str, float | None] = {}
        if "lowest_price" in item:
            prices["lowest_price"] = self.price_to_float(item["lowest_price"])

        if "median_price" in item:
            prices["median_price"] = self.price_to_float(item["median_price"])

        return prices or None

    def get_lowest_price(self, name: str, app_id: int | AppID) -> float | None:
        """
        Gets the lowest price of an item.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :param app_id: The AppID of the game the item is from.
        :type app_id: :class:`int`, :class:`AppID`
        :return: The lowest price of the item, if suceess. :class: `None` otherwise.
        :rtype: :class:`float`, :class:`None`

        .. versionchanged:: 1.2.4
        .. versionadded:: 1.2.0
        """

        return self.get_price(name, app_id, "lowest_price")

    def get_median_price(self, name: str, app_id: int | AppID) -> float | None:
        """
        Gets the median price of an item.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :param app_id: The AppID of the game the item is from.
        :type app_id: :class:`int`, :class:`AppID`
        :return: The median price of the item, if suceess. :class: `None` otherwise.
        :rtype: :class:`float`, :class:`None`

        .. versionchanged:: 1.2.4
        .. versionadded:: 1.2.0
        """

        return self.get_price(name, app_id, "median_price")

    def get_price(self, name: str, app_id: int | AppID, type: str) -> float | None:
        """
        Gets the lowest or median price of an item.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :param app_id: The AppID of the game the item is from.
        :type app_id: :class:`int`, :class:`AppID`
        :param type: The type of price. Can be either ``"lowest_price"`` or ``"median_price"``.
        :type type: :class:`str`
        :return: The price of the item, if suceess. :class: `None` otherwise.
        :rtype: :class:`float`, :class:`None`

        .. versionadded:: 1.2.4
        """

        item = self.get_overview(name, app_id)
        if item is None:
            return None

        return self.price_to_float(item[type]) if type in item else None

    def get_volume(self, name: str, app_id: int | AppID) -> int | None:
        """
        Gets the volume of an item.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :param app_id: The AppID of the game the item is from.
        :type app_id: :class:`int`, :class:`AppID`
        :return: The volume if success, :class:`None` otherwise.
        :rtype: :class:`int`, :class:`None`

        .. versionchanged:: 1.2.4
        .. versionadded:: 1.2.0
        """

        item = self.get_overview(name, app_id)
        if item is None:
            return None

        return int(item["volume"].replace(",", "")) if "volume" in item else None

    def has_invalid_name(self, name: str) -> bool:
        """
        Checks if given item name is invalid.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :return: :class:`True` if the item name is invalid, :class:`False` otherwise.
        :rtype: :class:`bool`

        .. versionadded:: 1.1.0
        """

        if isinstance(name, str):
            try:
                return name.index("/") >= 0
            except ValueError:
                return False

        raise TypeError(f'"name" must be "str", not "{type(name)}".')

    def fix_name(self, name: str) -> str:
        """
        Replaces "/" with "-" and returns the item name.

        :param name: The name of the item how it appears on the Steam Community Market.
        :type name: :class:`str`
        :return: The correct item name.
        :rtype: :class:`str`

        .. versionadded:: 1.1.0
        """

        if isinstance(name, str):
            return name.replace("/", "-")

        raise TypeError(f'"name" must be "str", not "{type(name)}".')

    def price_to_float(self, value: str) -> float | None:
        """
        Converts a price from :class:`str` to :class:`float`

        :param value: A price
        :type value: :class:`str`
        :return: :class:`float`
        :rtype: :class:`float`, :class:`None`

        .. versionchanged:: 1.2.4
        """

        if not (match := re.search(r"\d{1,3}(?:[\.,]\d{1,3})*([\.,])\d{2}", value)):
            return None

        delimiter = match[1]
        return (
            float(match.group())
            if delimiter == "."
            else float(match.group().replace(".", "").replace(",", "."))
        )
