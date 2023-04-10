import re
from steam_community_market.currencies import SteamCurrency, SteamLegacyCurrency
from steam_community_market.enums import AppID
from steam_community_market.exceptions import (
    InvalidCurrencyException,
    LegacyCurrencyException,
)
from steam_community_market.request import request
from typing import Optional, Union


class Market:
    """A class representing a Steam Community Market object.

    It allows users to get price and volume information for items in the Steam Community Market and supports multiple currencies.
    """

    URI = "http://steamcommunity.com/market/priceoverview"

    def __init__(
        self,
        currency: Union[
            int, str, SteamCurrency, SteamLegacyCurrency
        ] = SteamCurrency.USD,
    ) -> None:
        """Initializes the Market object with a specified currency.

        :param currency: Currency used for prices.
        :type currency: int or str or :class:`SteamCurrency` or :class:`SteamLegacyCurrency`
        :value currency: :class:`SteamCurrency`.:attr:`USD`
        :raises :class:`InvalidCurrencyException`: Raised when a currency is considered to be invalid by the Steam Community Market.
        :raises :class:`LegacyCurrencyException`: Raised when a currency is not supported by the Steam Community Market anymore.
        """

        self.currency = self._supported_currency(currency)

    def get_overview(
        self, app_id: Union[int, AppID], market_hash_name: str
    ) -> Optional[dict[str, Union[bool, str]]]:
        """Gets the prices and volume of an item in the Steam Community Market.

        .. versionadded:: 1.0.0
        .. versionchanged:: 1.3.0
            * Moved :param:`app_id` on the first position.
            * Renamed :param:`name` to :param:`market_hash_name`.
            * Moved :param:`app_id`'s validation to :meth:`_app_id_value`.
            * Improved type hinting for both parameters and return value.
            * Removed :param:`market_hash_name`'s validation check and just called :meth:`_fix_item_name`.
            * Simplified the return statement.

        :param app_id: The App ID of the game the item is from.
        :type app_id: int or AppID
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :raises TypeError: Raised when :param:`market_hash_name` is not a string.
        :return: An overview of the item on success, :class:`None` otherwise. Overview includes both volume and prices.
        :rtype: dict[str, bool or str] or None
        """

        if not isinstance(market_hash_name, str):
            raise TypeError(
                f'"market_hash_name" must be "str", not "{type(market_hash_name)}".'
            )

        app_id = self._app_id_value(app_id)
        market_hash_name = self._fix_item_name(market_hash_name)

        payload = {
            "appid": app_id,
            "market_hash_name": market_hash_name,
            "currency": self.currency.value,
        }
        response = request(self.URI, payload)

        return None if not response or response["success"] == False else response

    def get_overviews(
        self,
        app_id: Union[int, list[Union[int, AppID]], AppID],
        market_hash_names: list[str],
    ) -> dict[str, dict[str, Union[bool, str]]]:
        """Gets the prices and volumes of multiple items in the Steam Community Market.
        
        .. versionadded:: 1.0.0
        .. versionchanged:: 1.3.0
            * Moved :param:`app_id` on the first position.
            * Renamed :param:`names` to :param:`market_hash_names`.
            * Moved :param:`app_id`'s validation to :meth:`_app_id_value`.
            * Improved type hinting for both parameters and return value.
            * Implemented usage of list-comprehension for the return value.
        
        :param app_id: If given a list, it needs to have the same length as the :param:`market_hash_names`. \
            If given :class:`int` or :class:`AppID`, every item in `names` must have this App ID.
        :type app_id: int or list[int or :class:`AppID`] or :class:`AppID`
        :param market_hash_names: A list of item names how they appear on the Steam Community Market.
        :type market_hash_names: list[str]
        :raises IndexError: Raised when :param:`market_hash_names` and :param:`app_id` have different lengths.
        :return: An overview of each item. 
        :rtype: dict[str, dict[str, bool or str]]
        """

        prices = {}
        app_id = self._app_id_value(app_id, support_lists=True)
        if isinstance(app_id, list):
            if len(market_hash_names) == len(app_id):
                prices = {
                    name: self.get_overview(id, name)
                    for name, id in zip(market_hash_names, app_id)
                }
            else:
                raise IndexError(
                    '"market_hash_names" and "app_id" must have the same length.'
                )

        else:
            prices = {
                name: self.get_overview(app_id, name) for name in market_hash_names
            }

        return prices

    def get_overviews_from_dict(
        self, items: dict[Union[int, AppID], list[str]]
    ) -> dict[str, dict[str, Union[bool, str]]]:
        """Gets the prices and volumes of multiple items in the Steam Community Market from a dictionary.
        
        .. versionadded:: 1.1.0
        .. versionchanged:: 1.3.0
            * Improved type hinting for both parameters and return value.
            * Simplified the accepted format of the :param:`items` parameter.
            * Simplified the return statement by using list-comprehension.
        
        :param items: A dictionary containing item names and App IDs. There is an \
            example on how this dictionary should be constructed in ``example.py``.
        :type items: dict[int or :class:`AppID`, list[str]]
        :raises TypeError: Raised when :param:`items` is not a :class:`dict`.
        :return: An overview of each item.
        :rtype: dict[str, dict[str, bool or str]]
        """

        if not isinstance(items, dict):
            raise TypeError(f'"items" must be "dict", not "{type(items)}".')

        return {
            name: self.get_overview(app_id, name)
            for app_id, names in items.items()
            for name in names
        }

    def get_prices(
        self, app_id: Union[int, AppID], market_hash_name: str
    ) -> Optional[dict[str, Optional[float]]]:
        """Gets the lowest and/or median price of an item in the Steam Community Market, if they exist.

        .. versionadded:: 1.2.0
        .. versionchanged:: 1.3.0
            * Moved :param:`app_id` on the first position.
            * Renamed :param:`name` to :param:`market_hash_name`.
            * Improved type hinting for both parameters and return value.
            * :class:`None` comparison is now done with ``is`` instead of ``==``.
            * Simplified the return statement.

        :param app_id: The App ID of the game the item is from.
        :type app_id: int or :class:`AppID`
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :return: The lowest and/or median price of the item, if suceess. :class:`None` otherwise.
        :rtype: dict[str, floar or None] or None
        """

        item = self.get_overview(app_id, market_hash_name)

        if item is None:
            return None

        prices: dict[str, Optional[float]] = {}
        if "lowest_price" in item:
            prices["lowest_price"] = self._price_to_float(item["lowest_price"])

        if "median_price" in item:
            prices["median_price"] = self._price_to_float(item["median_price"])

        return prices or None

    def get_lowest_price(
        self, app_id: Union[int, AppID], market_hash_name: str
    ) -> Optional[float]:
        """Gets the lowest price of an item in the Steam Community Market, if is exists.

        .. versionadded:: 1.2.0
        .. versionchanged:: 1.3.0
            * Moved :param:`app_id` on the first position.
            * Renamed :param:`name` to :param:`market_hash_name`.
            * Improved type hinting for both parameters and return value.
            * Moved functionality to :meth:`get_price`.

        :param app_id: The App ID of the game the item is from.
        :type app_id: int or :class:`AppID`
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :return: The lowest price of the item, if suceess. :class:`None` otherwise.
        :rtype: float or None
        """

        return self.get_price(app_id, market_hash_name, "lowest_price")

    def get_median_price(
        self, app_id: Union[int, AppID], market_hash_name: str
    ) -> Optional[float]:
        """Gets the median price of an item in the Steam Community Market, if it exists.

        .. versionadded:: 1.2.0
        .. versionchanged:: 1.3.0
            * Moved :param:`app_id` on the first position.
            * Renamed :param:`name` to :param:`market_hash_name`.
            * Improved type hinting for both parameters and return value.
            * Moved functionality to :meth:`get_price`.

        :param app_id: The App ID of the game the item is from.
        :type app_id: int or :class:`AppID`
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :return: The median price of the item, if suceess. :class:`None` otherwise.
        :rtype: float or None
        """

        return self.get_price(app_id, market_hash_name, "median_price")

    def get_price(
        self, app_id: Union[int, AppID], market_hash_name: str, type: str
    ) -> Optional[float]:
        """Gets the lowest or median price of an item.

        .. versionadded:: 1.3.0

        :param app_id: The App ID of the game the item is from.
        :type app_id: int or :class:`AppID`
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param type: The type of price. Can be either ``lowest_price`` or ``median_price``.
        :type type: str
        :return: The price of the item, if suceess. :class:`None` otherwise.
        :rtype: float or None
        """

        item = self.get_overview(app_id, market_hash_name)
        if item is None:
            return None

        return self._price_to_float(item[type]) if type in item else None

    def get_volume(
        self, app_id: Union[int, AppID], market_hash_name: str
    ) -> Optional[int]:
        """Gets the volume of an item in the Steam Community Market, if it exists.

        .. versionadded:: 1.2.0
        .. versionchanged:: 1.3.0
            * Improved type hinting for both parameters and return value.
            * :class:`None` comparison is now done with ``is`` instead of ``==``.
            * Simplified the return statement.

        :param app_id: The App ID of the game the item is from.
        :type app_id: int or :class:`AppID`
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :return: The volume if success, :class:`None` otherwise.
        :rtype: int or None
        """

        item = self.get_overview(app_id, market_hash_name)
        if item is None:
            return None

        return int(item["volume"].replace(",", "")) if "volume" in item else None

    @staticmethod
    def _app_id_value(
        app_id: Union[int, list[Union[int, AppID]], AppID], support_lists: bool = False
    ) -> int:
        """Validates and returns the value of an AppID.

        .. versionadded:: 1.3.0

        :param app_id: The App ID of the game the item is from.
        :type app_id: int or list[int or :class:`AppID`] or :class:`AppID`
        :param support_lists: Whether or not to support lists.
        :type support_lists: bool
        :raises TypeError: Raised when :param:`app_id` is not a supported type.
        :return: The value of the App ID.
        :rtype: int
        """

        if isinstance(app_id, AppID):
            return app_id.value
        if isinstance(app_id, int) or (
            support_lists
            and isinstance(app_id, list)
            and all(isinstance(id, int or AppID) for id in app_id)
        ):
            return app_id

        raise TypeError(
            support_lists
            and f'"app_id" must be "int", "list" or "AppID", not "{type(app_id)}".'
            or f'"app_id" must be "int" or "AppID", not "{type(app_id)}".'
        )

    @staticmethod
    def _fix_item_name(market_hash_name: str) -> str:
        """Replaces "/" with "-" and returns the item name.

        .. versionadded:: 1.1.0
        .. versionchanged:: 1.3.0
           Transformed into a static method and renamed it from ``fix_name`` to ``_fix_item_name``.

        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :raises TypeError: If the given :param:`market_hash_name` is not a string.
        :return: The correct item name.
        :rtype: str
        """

        if isinstance(market_hash_name, str):
            return market_hash_name.replace("/", "-")

        raise TypeError(f'"name" must be "str", not "{type(market_hash_name)}".')

    @staticmethod
    def _price_to_float(value: str) -> Optional[float]:
        """Converts a price from string to float.

        .. versionchanged:: 1.3.0
           * Added better parsing for strings using Regex.
           * Added support for price values with a comma as the decimal delimiter.

        :param value: A price in string format.
        :type value: str
        :return: The price in float format.
        :rtype: float or None
        """

        if not (match := re.search(r"\d{1,3}(?:([\.,])\d{1,3})*(?:\1\d{2})?", value)):
            return None

        delimiter = match[1]
        return (
            float(match[0].replace(",", ""))
            if delimiter == "."
            else float(match[0].replace(".", "").replace(",", "."))
        )

    @staticmethod
    def _supported_currency(
        currency: Union[int, str, SteamCurrency, SteamLegacyCurrency],
    ) -> SteamCurrency:
        """Returns a supported currency.

        .. versionadded:: 1.3.0

        :param currency: Currency used for prices.
        :type currency: int or str or :class:`SteamCurrency` or :class:`SteamLegacyCurrency`
        :raises :class:`InvalidCurrencyException`: Raised when a currency is considered to be invalid by the Steam Community Market.
        :raises :class:`LegacyCurrencyException`: Raised when a currency is not supported by the Steam Community Market anymore.
        :return: A supported currency.
        :rtype: :class:`SteamCurrency`
        """

        result: Union[SteamCurrency, None] = None
        if isinstance(currency, int) and currency in SteamCurrency.__members__.values():
            result = SteamCurrency(currency)

        elif (
            isinstance(currency, str)
            and (currency := currency.upper()) in SteamCurrency.__members__.keys()
        ):
            result = SteamCurrency[currency]

        elif isinstance(currency, SteamCurrency):
            result = currency

        if result is None:
            raise InvalidCurrencyException(currency)

        elif (
            isinstance(currency, SteamLegacyCurrency)
            or result.name in SteamLegacyCurrency.__members__.keys()
            or result.value in SteamLegacyCurrency.__members__.values()
        ):
            raise LegacyCurrencyException(currency)

        return result
