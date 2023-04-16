import re

from .currencies import SteamCurrency, SteamLegacyCurrency
from .enums import AppID
from .exceptions import (
    InvalidCurrencyException,
    LegacyCurrencyException,
)
from .request import _request_overview

from typing import Optional, Union


class Market:
    """A class representing a Steam Community Market object.

    It allows users to get price and volume information for items in the Steam Community Market and supports multiple currencies.
    """

    def __init__(
        self,
        currency: Union[
            int, str, SteamCurrency, SteamLegacyCurrency
        ] = SteamCurrency.USD,
    ) -> None:
        """Initializes the Market object with a specified currency.

        .. currentmodule:: steam_community_market.currencies

        :param currency: Currency used for prices. Defaults to :attr:`SteamCurrency.USD`.
        :type currency: int or str or SteamCurrency or SteamLegacyCurrency
        :raises InvalidCurrencyException: Raised when a currency is considered to be invalid by the Steam Community Market.
        :raises LegacyCurrencyException: Raised when a currency is not supported by the Steam Community Market anymore.
        """

        self.currency = self._supported_currency(currency)

    def get_overview(
        self,
        app_id: Union[int, AppID],
        market_hash_name: str,
        type_conversion: bool = True,
    ) -> Optional[dict[str, Union[bool, float, int, str]]]:
        """Gets the prices and volume of an item in the Steam Community Market.

        .. currentmodule:: steam_community_market.enums

        :param app_id: The :class:`AppID` of the game the item is from.
        :type app_id: int or AppID
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: An overview of the item on success, :obj:`None` otherwise. Overview includes both volume and prices.
        :rtype: dict[str, bool or float or int or str] or None
        :raises InvalidItemOrAppIDException: Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        :raises TooManyRequestsException: Raised when the request limit has been reached.
        :raises TypeError: Raised when ``market_hash_name`` is not a string.

        .. versionchanged:: 1.3.0
        .. versionadded:: 1.0.0
        """

        if not isinstance(market_hash_name, str):
            raise TypeError(
                f'"market_hash_name" must be "str", not "{type(market_hash_name)}".'
            )

        data = _request_overview(app_id, market_hash_name, self.currency)
        # if data is None:
        #     # TODO: Raise an exception instead?
        if type_conversion:
            data = self._overview_type_converter(data)

        return data

    def get_overviews(
        self,
        app_id: Union[int, list[Union[int, AppID]], AppID],
        market_hash_names: list[str],
        type_conversion: bool = True,
    ) -> dict[str, dict[str, Union[bool, str]]]:
        """Gets the prices and volumes of multiple items in the Steam Community Market.
        
        .. currentmodule:: steam_community_market.enums
        
        :param app_id: If given a list, it needs to have the same length as the ``market_hash_names``. \
            If given :obj:`int` or :class:`AppID`, every item in ``market_hash_names`` must have this :class:`AppID`.
        :type app_id: int or list[int or AppID] or AppID
        :param market_hash_names: A list of item names how they appear on the Steam Community Market.
        :type market_hash_names: list[str]
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: An overview of each item. 
        :rtype: dict[str, dict[str, bool or str]]
        :raises IndexError: Raised when ``app_id`` and ``market_hash_names`` have different lengths.
        :raises TooManyRequestsException: Raised when the request limit has been reached.
        
        .. versionchanged:: 1.3.0
        .. versionadded:: 1.0.0
        """

        prices = {}
        if isinstance(app_id, list):
            if len(market_hash_names) == len(app_id):
                prices = {
                    name: self._overview_type_converter(
                        _request_overview(
                            id, name, self.currency, raise_exception=False
                        )
                    )
                    if type_conversion
                    else _request_overview(
                        id, name, self.currency, raise_exception=False
                    )
                    for name, id in zip(market_hash_names, app_id)
                }
            else:
                raise IndexError(
                    '"market_hash_names" and "app_id" must have the same length.'
                )

        else:
            prices = {
                name: self._overview_type_converter(
                    _request_overview(
                        app_id, name, self.currency, raise_exception=False
                    )
                )
                if type_conversion
                else _request_overview(
                    app_id, name, self.currency, raise_exception=False
                )
                for name in market_hash_names
            }

        return prices

    def get_overviews_from_dict(
        self, items: dict[Union[int, AppID], list[str]], type_conversion: bool = True
    ) -> dict[str, dict[str, Union[bool, str]]]:
        """Gets the prices and volumes of multiple items in the Steam Community Market from a dictionary.
        
        .. currentmodule:: steam_community_market.enums
        
        :param items: A dictionary containing :class:`AppID` as `keys` and a list of item names as `values`. There is an \
            example on how this dictionary should be constructed in ``example.py``.
        :type items: dict[int or AppID, list[str]]
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: An overview of each item.
        :rtype: dict[str, dict[str, bool or str]]
        :raises TooManyRequestsException: Raised when the request limit has been reached.
        :raises TypeError: Raised when ``items`` is not a :obj:`dict`.
        
        .. versionchanged:: 1.3.0
        .. versionadded:: 1.1.0
        """

        if not isinstance(items, dict):
            raise TypeError(f'"items" must be "dict", not "{type(items)}".')

        return {
            name: self._overview_type_converter(
                _request_overview(
                    app_id,
                    name,
                    self.currency,
                    raise_exception=False,
                )
            )
            if type_conversion
            else _request_overview(
                app_id,
                name,
                self.currency,
                raise_exception=False,
            )
            for app_id, names in items.items()
            for name in names
        }

    def get_prices(
        self,
        app_id: Union[int, AppID],
        market_hash_name: str,
        type_conversion: bool = True,
    ) -> Optional[dict[str, Union[float, str]]]:
        """Gets the lowest and/or median price of an item in the Steam Community Market, if they exist.

        .. currentmodule:: steam_community_market.enums

        :param app_id: The :class:`AppID` of the game the item is from.
        :type app_id: int or AppID
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: The lowest and/or median price of the item, if suceess. :obj:`None` otherwise.
        :rtype: dict[str, float or str] or None
        :raises InvalidItemOrAppIDException: Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        :raises TooManyRequestsException: Raised when the request limit has been reached.

        .. versionchanged:: 1.3.0
        .. versionadded:: 1.2.0
        """

        item = _request_overview(app_id, market_hash_name, self.currency)
        if item is None:
            return None

        prices: dict[str, Optional[float]] = {}
        if "lowest_price" in item:
            prices["lowest_price"] = (
                self._price_to_float(item["lowest_price"])
                if type_conversion
                else item["lowest_price"]
            )

        if "median_price" in item:
            prices["median_price"] = (
                self._price_to_float(item["median_price"])
                if type_conversion
                else item["median_price"]
            )

        return prices or None

    def get_lowest_price(
        self,
        app_id: Union[int, AppID],
        market_hash_name: str,
        type_conversion: bool = True,
    ) -> Optional[float]:
        """Gets the lowest price of an item in the Steam Community Market, if is exists.

        .. currentmodule:: steam_community_market.enums

        :param app_id: The :class:`AppID` of the game the item is from.
        :type app_id: int or AppID
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: The lowest price of the item, if suceess. :obj:`None` otherwise.
        :rtype: float or None
        :raises InvalidItemOrAppIDException: Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        :raises TooManyRequestsException: Raised when the request limit has been reached.

        .. versionchanged:: 1.3.0
        .. versionadded:: 1.2.0
        """

        return self.get_price(app_id, market_hash_name, "lowest_price", type_conversion)

    def get_median_price(
        self,
        app_id: Union[int, AppID],
        market_hash_name: str,
        type_conversion: bool = True,
    ) -> Optional[float]:
        """Gets the median price of an item in the Steam Community Market, if it exists.

        .. currentmodule:: steam_community_market.enums

        :param app_id: The :class:`AppID` of the game the item is from.
        :type app_id: int or AppID
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: The median price of the item, if suceess. :obj:`None` otherwise.
        :rtype: float or None
        :raises InvalidItemOrAppIDException: Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        :raises TooManyRequestsException: Raised when the request limit has been reached.

        .. versionchanged:: 1.3.0
        .. versionadded:: 1.2.0
        """

        return self.get_price(app_id, market_hash_name, "median_price", type_conversion)

    def get_price(
        self,
        app_id: Union[int, AppID],
        market_hash_name: str,
        type: str,
        type_conversion: bool = True,
    ) -> Optional[float]:
        """Gets the lowest or median price of an item.

        .. currentmodule:: steam_community_market.enums

        :param app_id: The :class:`AppID` of the game the item is from.
        :type app_id: int or AppID
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param type: The type of price. Can be either ``lowest_price`` or ``median_price``.
        :type type: str
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: The price of the item, if suceess. :obj:`None` otherwise.
        :rtype: float or None
        :raises InvalidItemOrAppIDException: Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        :raises TooManyRequestsException: Raised when the request limit has been reached.

        .. versionadded:: 1.3.0
        """

        item = _request_overview(app_id, market_hash_name, self.currency)
        if item is None:
            return None

        result = self._price_to_float(item[type]) if type_conversion else item[type]
        return result if type in item else None

    def get_volume(
        self,
        app_id: Union[int, AppID],
        market_hash_name: str,
        type_conversion: bool = True,
    ) -> Optional[int]:
        """Gets the volume of an item in the Steam Community Market, if it exists.

        .. currentmodule:: steam_community_market.enums

        :param app_id: The :class:`AppID` of the game the item is from.
        :type app_id: int or AppID
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: The volume if success, :obj:`None` otherwise.
        :rtype: int or None
        :raises InvalidItemOrAppIDException: Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        :raises TooManyRequestsException: Raised when the request limit has been reached.

        .. versionchanged:: 1.3.0
        .. versionadded:: 1.2.0
        """

        item = _request_overview(app_id, market_hash_name, self.currency)
        if item is None:
            return None

        result = (
            int(item["volume"].replace(",", "")) if type_conversion else item["volume"]
        )
        return result if "volume" in item else None

    @staticmethod
    def _overview_type_converter(
        overview: dict, keys_to_convert: list[str] = None
    ) -> dict[str, Union[str, int, float]]:
        """Converts the type of the values of an overview.

        :param overview: The overview of an item.
        :type overview: dict
        :param keys_to_convert: The keys to convert.
        :type keys_to_convert: list[str]
        :return: The converted overview.
        :rtype: dict
        :raises ValueError: Raised when ``keys_to_convert`` contains an invalid key.

        .. versionadded:: 1.3.0
        """

        valid_keys = ["lowest_price", "median_price", "volume"]
        if keys_to_convert is None:
            keys_to_convert = valid_keys

        if any(key not in valid_keys for key in keys_to_convert):
            raise ValueError(
                f'Invalid key found in "keys_to_convert". The valid keys are: {", ".join(valid_keys)}.'
            )

        result = {}
        for key, value in overview.items():
            if key in keys_to_convert and key in ["lowest_price", "median_price"]:
                result[key] = Market._price_to_float(value)
            elif key in keys_to_convert and key == "volume":
                result[key] = int(value.replace(",", ""))
            else:
                result[key] = value

        return result

    @staticmethod
    def _price_to_float(value: str) -> Optional[float]:
        """Converts a price from string to float.

        :param value: A price in string format.
        :type value: str
        :return: The price in float format.
        :rtype: float or None

        .. versionchanged:: 1.3.0
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

        .. currentmodule:: steam_community_market.currencies

        :param currency: Currency used for prices.
        :type currency: int or str or :class:`SteamCurrency` or :class:`SteamLegacyCurrency`
        :return: A supported currency.
        :rtype: SteamCurrency
        :raises InvalidCurrencyException: Raised when a currency is considered to be invalid by the Steam Community Market.
        :raises LegacyCurrencyException: Raised when a currency is not supported by the Steam Community Market anymore.

        .. versionadded:: 1.3.0
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
