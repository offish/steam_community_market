import re

from .currencies import SteamCurrency, SteamLegacyCurrency
from .enums import AppID, SteamLanguage
from .exceptions import (
    InvalidLanguageException,
    InvalidCurrencyException,
    LegacyCurrencyException,
)
from .requests import _request_overview

from typing import Optional, Union


class Market:
    """A class representing a Steam Community Market object.

    It allows users to interact with the Steam Community Market API, by providing methods to get different information about items in the market. \
        It supports all currencies and languages that are supported by the Steam Community Market API.

    .. currentmodule:: steam_community_market.currencies

    :param currency: Currency used for prices. Defaults to :attr:`SteamCurrency.USD`.
    :type currency: SteamCurrency or SteamLegacyCurrency or int or str
    :param language: Language used for the returned data. Defaults to :attr:`SteamLanguage.ENGLISH`.
    :type language: SteamLanguage or int or str
    :raises InvalidCurrencyException: Raised when the ``currency`` is invalid.
    :raises LegacyCurrencyException: Raised when the ``currency`` is a legacy currency.
    :raises InvalidLanguageException: Raised when the ``language`` is invalid.
    """

    def __init__(
        self,
        currency: Union[
            SteamCurrency, SteamLegacyCurrency, int, str
        ] = SteamCurrency.USD,
        language: Union[SteamLanguage, str] = SteamLanguage.ENGLISH,
    ) -> None:
        self.currency = self._supported_currency(currency)
        self.language = self._valid_language(language)

    def get_overview(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
    ) -> Optional[dict[str, Union[bool, float, int, str]]]:
        """Gets the prices and volume of an item in the Steam Community Market.

        .. currentmodule:: steam_community_market.enums

        :param app_id: The :class:`AppID` of the game the item is from.
        :type app_id: AppID or int
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: An overview of the item on success, :obj:`None` otherwise. Overview includes both volume and prices.
        :rtype: dict[str, bool or float or int or str] or None
        :raises InvalidItemOrAppIDException: Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        :raises TooManyRequestsException: Raised when the request limit has been reached.
        :raises TypeError: Raised when any of the parameters are of the wrong type.

        .. versionchanged:: 1.3.0
        .. versionadded:: 1.0.0
        """

        self._validate_overview_parameters(app_id, market_hash_name, type_conversion)

        data = _request_overview(app_id, market_hash_name, self.currency)
        # if data is None:
        #     # TODO: Raise an exception instead?
        if type_conversion:
            data = self._overview_type_converter(data)

        return data

    def get_overviews(
        self,
        app_id: Union[AppID, int, list[Union[AppID, int]]],
        market_hash_names: list[str],
        type_conversion: bool = True,
    ) -> dict[str, dict[str, Union[bool, str]]]:
        """Gets the prices and volumes of multiple items in the Steam Community Market.
        
        .. currentmodule:: steam_community_market.enums
        
        :param app_id: If given a list, it needs to have the same length as the ``market_hash_names``. \
            If given :obj:`int` or :class:`AppID`, every item in ``market_hash_names`` must have this :class:`AppID`.
        :type app_id: AppID or int or list[AppID or int]
        :param market_hash_names: A list of item names how they appear on the Steam Community Market.
        :type market_hash_names: list[str]
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: An overview of each item. 
        :rtype: dict[str, dict[str, bool or str]]
        :raises IndexError: Raised when ``app_id`` and ``market_hash_names`` have different lengths.
        :raises TooManyRequestsException: Raised when the request limit has been reached.
        :raises TypeError: Raised when any of the parameters are of the wrong type.
        
        .. versionchanged:: 1.3.0
        .. versionadded:: 1.0.0
        """

        self._validate_overview_parameters(
            app_id, market_hash_names, type_conversion, support_lists=True
        )

        if not isinstance(app_id, list):
            app_id = [app_id] * len(market_hash_names)

        if len(market_hash_names) != len(app_id):
            raise IndexError(
                'The length of "market_hash_names" and "app_id" must be the same.'
            )

        return {
            name: (self._overview_type_converter(result) if type_conversion else result)
            for name, id in zip(market_hash_names, app_id)
            for result in [
                _request_overview(id, name, self.currency, raise_exception=False)
            ]
        }

    def get_overviews_from_dict(
        self, items: dict[Union[AppID, int], list[str]], type_conversion: bool = True
    ) -> dict[str, dict[str, Union[bool, str]]]:
        """Gets the prices and volumes of multiple items in the Steam Community Market from a dictionary.
        
        .. currentmodule:: steam_community_market.enums
        
        :param items: A dictionary containing :class:`AppID` as `keys` and a list of item names as `values`. There is an \
            example on how this dictionary should be constructed in ``example.py``.
        :type items: dict[AppID or int, list[str]]
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: An overview of each item.
        :rtype: dict[str, dict[str, bool or str]]
        :raises TooManyRequestsException: Raised when the request limit has been reached.
        :raises TypeError: Raised when any of the parameters are of the wrong type.
        
        .. versionchanged:: 1.3.0
        .. versionadded:: 1.1.0
        """

        if not isinstance(items, dict) or not all(
            isinstance(app_id, (AppID, int))
            and isinstance(market_hash_names, list)
            and isinstance(name, str)
            for app_id, market_hash_names in items.items()
            for name in market_hash_names
        ):
            raise TypeError(
                f'The type of "items" must be "dict[Union[AppID, int], list[str]]", not "{type(items)}".'
            )

        self._validate_type_conversion(type_conversion)

        result = {}
        for app_id, names in items.items():
            for name in names:
                overview = _request_overview(
                    app_id, name, self.currency, raise_exception=False
                )
                if type_conversion:
                    overview = self._overview_type_converter(overview)

                result[name] = overview

        return result

    def get_prices(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
    ) -> Optional[dict[str, Union[float, str]]]:
        """Gets the lowest and/or median price of an item in the Steam Community Market, if they exist.

        .. currentmodule:: steam_community_market.enums

        :param app_id: The :class:`AppID` of the game the item is from.
        :type app_id: AppID or int
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: The lowest and/or median price of the item, if suceess. :obj:`None` otherwise.
        :rtype: dict[str, float or str] or None
        :raises InvalidItemOrAppIDException: Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        :raises TooManyRequestsException: Raised when the request limit has been reached.
        :raises TypeError: Raised when any of the parameters are of the wrong type.

        .. versionchanged:: 1.3.0
        .. versionadded:: 1.2.0
        """

        self._validate_overview_parameters(app_id, market_hash_name, type_conversion)

        item = _request_overview(app_id, market_hash_name, self.currency)
        if item is None:
            return None

        price_keys = ["lowest_price", "median_price"]
        prices = {
            key: (self._price_to_float(item[key]) if type_conversion else item[key])
            for key in price_keys
            if key in item
        }

        return prices or None

    def get_lowest_price(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
    ) -> Optional[float]:
        """Gets the lowest price of an item in the Steam Community Market, if is exists.

        .. currentmodule:: steam_community_market.enums

        :param app_id: The :class:`AppID` of the game the item is from.
        :type app_id: AppID or int
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: The lowest price of the item, if suceess. :obj:`None` otherwise.
        :rtype: float or None
        :raises InvalidItemOrAppIDException: Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        :raises TooManyRequestsException: Raised when the request limit has been reached.
        :raises TypeError: Raised when any of the parameters are of the wrong type.

        .. versionchanged:: 1.3.0
        .. versionadded:: 1.2.0
        """

        self._validate_overview_parameters(app_id, market_hash_name, type_conversion)
        return self.get_price(
            app_id,
            market_hash_name,
            "lowest_price",
            type_conversion,
            skip_validation=True,
        )

    def get_median_price(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
    ) -> Optional[float]:
        """Gets the median price of an item in the Steam Community Market, if it exists.

        .. currentmodule:: steam_community_market.enums

        :param app_id: The :class:`AppID` of the game the item is from.
        :type app_id: AppID or int
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: The median price of the item, if suceess. :obj:`None` otherwise.
        :rtype: float or None
        :raises InvalidItemOrAppIDException: Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        :raises TooManyRequestsException: Raised when the request limit has been reached.
        :raises TypeError: Raised when any of the parameters are of the wrong type.

        .. versionchanged:: 1.3.0
        .. versionadded:: 1.2.0
        """

        self._validate_overview_parameters(app_id, market_hash_name, type_conversion)
        return self.get_price(
            app_id,
            market_hash_name,
            "median_price",
            type_conversion,
            skip_validation=True,
        )

    def get_price(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        price_type: str,
        type_conversion: bool = True,
        **kwargs,
    ) -> Optional[float]:
        """Gets the lowest or median price of an item.

        .. currentmodule:: steam_community_market.enums

        :param app_id: The :class:`AppID` of the game the item is from.
        :type app_id: AppID or int
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param price_type: The type of price. Can be either ``lowest_price`` or ``median_price``.
        :type price_type: str
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: The price of the item, if suceess. :obj:`None` otherwise.
        :rtype: float or None
        :raises InvalidItemOrAppIDException: Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        :raises TooManyRequestsException: Raised when the request limit has been reached.
        :raises TypeError: Raised when any of the parameters are of the wrong type.
        :raises ValueError: Raised when ``price_type`` is not one of ``lowest_price`` or ``median_price``.

        .. versionadded:: 1.3.0
        """

        skip_validation = kwargs.get("skip_validation", False)
        if not skip_validation:
            self._validate_overview_parameters(
                app_id, market_hash_name, type_conversion
            )
            if not isinstance(price_type, str):
                raise TypeError(
                    f'The type of "price_type" must be "str", not "{type(price_type).__name__}".'
                )

            valid_price_types = ("lowest_price", "median_price")
            if price_type not in valid_price_types:
                raise ValueError(
                    f'The type of "price_type" must be one of {valid_price_types}, not "{price_type}".'
                )

        item = _request_overview(app_id, market_hash_name, self.currency)
        if item is None:
            return None

        result = (
            self._price_to_float(item[price_type])
            if type_conversion
            else item[price_type]
        )
        return result if price_type in item else None

    def get_volume(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
    ) -> Optional[int]:
        """Gets the volume of an item in the Steam Community Market, if it exists.

        .. currentmodule:: steam_community_market.enums

        :param app_id: The :class:`AppID` of the game the item is from.
        :type app_id: AppID or int
        :param market_hash_name: The name of the item how it appears on the Steam Community Market.
        :type market_hash_name: str
        :param type_conversion: Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        :type type_conversion: bool
        :return: The volume if success, :obj:`None` otherwise.
        :rtype: int or None
        :raises InvalidItemOrAppIDException: Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        :raises TooManyRequestsException: Raised when the request limit has been reached.
        :raises TypeError: Raised when any of the parameters are of the wrong type.

        .. versionchanged:: 1.3.0
        .. versionadded:: 1.2.0
        """

        self._validate_overview_parameters(app_id, market_hash_name, type_conversion)

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

        if not (match := re.search(r"(\d{1,3}(?:[.,]\d{3})*)(?:[.,](\d{2}))?", value)):
            return None

        num_str = match[1].replace(",", "").replace(".", "")
        decimal_part = match[2] if match[2] is not None else "00"
        return float(f"{num_str}.{decimal_part}")

    @staticmethod
    def _supported_currency(
        currency: Union[SteamCurrency, SteamLegacyCurrency, int, str],
    ) -> SteamCurrency:
        """Returns a supported currency.

        .. currentmodule:: steam_community_market.currencies

        :param currency: Currency used for prices.
        :type currency: SteamCurrency or SteamLegacyCurrency or int or str
        :return: A supported currency.
        :rtype: SteamCurrency
        :raises InvalidCurrencyException: Raised when a currency is considered to be invalid by the Steam Community Market.
        :raises LegacyCurrencyException: Raised when a currency is not supported by the Steam Community Market anymore.
        :raises TypeError: Raised when ``currency`` is not of type :class:`SteamCurrency`, :class:`SteamLegacyCurrency`, :obj:`int` or :obj:`str`.

        .. versionadded:: 1.3.0
        """

        if isinstance(currency, (SteamCurrency, SteamLegacyCurrency)):
            if isinstance(currency, SteamLegacyCurrency):
                raise LegacyCurrencyException(currency)

            return currency

        if isinstance(currency, str):
            currency = currency.upper()

        try:
            if isinstance(currency, int):
                currency = SteamCurrency(currency)

            elif currency in SteamLegacyCurrency:
                raise LegacyCurrencyException(currency)

            else:
                currency = SteamCurrency[currency]

        except KeyError as e:
            raise InvalidCurrencyException(currency) from e

        except ValueError as e:
            raise TypeError(
                f'The type of "currency" must be "int", "str", "SteamCurrency" or "SteamLegacyCurrency", not "{type(currency)}".'
            ) from e

        return currency

    @staticmethod
    def _valid_language(language: Union[SteamLanguage, str]) -> SteamLanguage:
        """Returns a Steam language object.

        .. currentmodule:: steam_community_market.enums

        :param language: The language to use.
        :type language: SteamLanguage or str
        :return: A Steam language object.
        :rtype: SteamLanguage
        :raises InvalidLanguageException: Raised when the language is invalid.
        :raises TypeError: Raised when ``language`` is not of type :class:`SteamLanguage` or :obj:`str`.

        .. versionadded:: 1.3.0
        """

        if isinstance(language, SteamLanguage):
            return language

        elif isinstance(language, str):
            matching_language = SteamLanguage.from_string(language)
            if matching_language is not None:
                return matching_language

        else:
            raise TypeError(
                f'The type of "language" must be "str" or "SteamLanguage", not "{type(language)}".'
            )

        raise InvalidLanguageException(language)

    @staticmethod
    def _validate_app_id(
        app_id: Union[AppID, int, list[Union[AppID, int]]], support_lists: bool
    ) -> None:
        """Validates an app ID parameter.

        :param app_id: The app ID to validate.
        :type app_id: AppID or int or list[AppID, int]
        :param support_lists: Whether to support lists.
        :type support_lists: bool
        :raises TypeError: Raised when ``app_id`` is not of type :class:`AppID`, :obj:`int` or :obj:`list` of :class:`AppID` and :obj:`int`.

        .. versionadded:: 1.3.0
        """

        valid_types = (AppID, int, list) if support_lists else (AppID, int)
        if not isinstance(app_id, valid_types) or (
            isinstance(app_id, list)
            and not all(isinstance(item, (AppID, int)) for item in app_id)
        ):
            raise TypeError(
                f'The type of "app_id" must be "AppID", "int"{", or list[AppID, int]" if support_lists else ""}, not "{type(app_id)}".'
            )

    @staticmethod
    def _validate_market_hash_name(
        market_hash_name: Union[str, list[str]], support_lists: bool
    ) -> None:
        """Validates a market hash name parameter.

        :param market_hash_name: The market hash name to validate.
        :type market_hash_name: str or list[str]
        :param support_lists: Whether to support lists.
        :type support_lists: bool
        :raises TypeError: Raised when ``market_hash_name`` is not of type :obj:`str` or :obj:`list` of :obj:`str`.

        .. versionadded:: 1.3.0
        """

        valid_type = list if support_lists else str
        if not isinstance(market_hash_name, valid_type) or (
            isinstance(market_hash_name, list)
            and not all(isinstance(item, str) for item in market_hash_name)
        ):
            raise TypeError(
                f'The type of "market_hash_name" must be {"list[str]" if support_lists else "str"}, not "{type(market_hash_name)}".'
            )

    @staticmethod
    def _validate_overview_parameters(
        app_id: Union[AppID, int, list[Union[AppID, int]]],
        market_hash_name: Union[str, list[str]],
        type_conversion: bool,
        support_lists: bool = False,
    ) -> None:
        """Validates the parameters for the overview method.

        .. currentmodule:: steam_community_market.market

        :param app_id: The app ID to validate.
        :type app_id: AppID or int or list[AppID, int]
        :param market_hash_name: The market hash name to validate.
        :type market_hash_name: str or list[str]
        :param support_lists: Whether to support lists.
        :type support_lists: bool
        :raises TypeError: Raised when any of the parameters is not of the correct type, besides ``support_lists``, \
            which helps validate :func:`Market.get_overviews`.

        .. versionadded:: 1.3.0
        """

        Market._validate_app_id(app_id, support_lists)
        Market._validate_market_hash_name(market_hash_name, support_lists)
        Market._validate_type_conversion(type_conversion)

    @staticmethod
    def _validate_type_conversion(type_conversion: bool) -> None:
        """Validates the type conversion parameter.

        :param type_conversion: The type conversion parameter to validate.
        :type type_conversion: bool
        :raises TypeError: Raised when ``type_conversion`` is not of type :obj:`bool`.

        .. versionadded:: 1.3.0
        """

        if not isinstance(type_conversion, bool):
            raise TypeError(
                f'The type of "type_conversion" must be "bool", not "{type(type_conversion)}".'
            )
