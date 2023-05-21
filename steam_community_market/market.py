from .currencies import Currency, LegacyCurrency
from .decorators import sanitized, typechecked
from .enums import AppID, Language
from .requests import _request_overview, exponential_backoff_strategy

from typing import Callable, Optional, Union

import re


class Market:
    """A class representing a Steam Community Market object.

    It allows users to interact with the Steam Community Market API, by providing methods to get different information about items in the market. \
        It supports all currencies and languages that are supported by the Steam Community Market API.

    Parameters
    ----------
    currency : Currency or LegacyCurrency or int or str
        Currency used for prices. Defaults to :attr:`Currency.USD <steam_community_market.currencies.Currency.USD>`.
    language : Language or int or str
        Language used for the returned data. Defaults to :attr:`Language.ENGLISH <steam_community_market.enums.Language.ENGLISH>`.
        
    Attributes
    ----------
    currency : Currency
        Currency used for prices.
    language : Language
        Language used for the returned data.
    
    Raises
    ------
    InvalidCurrencyException
        Raised when the ``currency`` is invalid.
    LegacyCurrencyException
        Raised when the ``currency`` is a legacy currency.
    InvalidLanguageException
        Raised when the ``language`` is invalid.
    TypeError
        Raised when any of the parameters are of the wrong type.
    """

    currency: Currency
    language: Language

    @typechecked
    @sanitized
    def __init__(
        self,
        currency: Union[Currency, LegacyCurrency, int, str] = Currency.USD,
        language: Union[Language, str] = Language.ENGLISH,
    ) -> None:
        self.currency = currency
        self.language = language

    @typechecked
    @sanitized
    def get_overview(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
    ) -> Optional[dict[str, Union[bool, float, int, str]]]:
        """Gets the prices and volume of an item on the Steam Community Market.

        .. versionchanged:: 1.3.0

        Parameters
        ----------
        app_id : AppID or int
            The app ID of the game the item is from.
        market_hash_name : str
            The name of the item; how it appears on the Steam Community Market.
        type_conversion : bool
            Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        currency : Currency or LegacyCurrency or int or str or None
            Currency used for prices. Defaults to the value imposed by the instance of the class.

        Raises
        ------
        InvalidItemOrAppIDException
            Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        TooManyRequestsException
            Raised when the request limit has been reached.
        TypeError
            Raised when any of the parameters are of the wrong type.

        Returns
        -------
        dict[str, bool or float or int or str] or None
            An overview of the item on success, :obj:`None` otherwise. Overview includes both volume and prices.
        """

        data = _request_overview(app_id, market_hash_name, currency or self.currency)
        if type_conversion:
            data = self._overview_type_converter(data)

        return data

    @typechecked
    @sanitized
    def get_overviews(
        self,
        app_id: Union[AppID, int, list[Union[AppID, int]]],
        market_hash_names: list[str],
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> dict[str, Optional[dict[str, Union[bool, float, int, str]]]]:
        """Gets the prices and volumes of one or more items on the Steam Community Market.
        
        .. versionchanged:: 1.3.0
        
        Parameters
        ----------
        app_id : AppID or int or list[AppID or int]
            If given a list, it needs to have the same length as ``market_hash_names``. If given :obj:`int` or \
            :class:`AppID <steam_community_market.enums.AppID>`, every item in ``market_hash_names`` must part of the same :class:`AppID <steam_community_market.enums>`.
        market_hash_names : list[str]
            A list of item names; how they appear on the Steam Community Market.
        type_conversion : bool
            Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        currency : Currency or LegacyCurrency or int or str or None
            Currency used for prices. Defaults to the value imposed by the instance of the class.
        rate_limit_handler : Callable[[int], tuple[bool, float]] or None
            A function that handles the rate limit. It should take one parameter, the number of seconds to wait, and return a tuple containing a \
            :obj:`bool` indicating whether the request should be retried and the number of seconds to wait. Defaults to \
            :func:`exponential_backoff_strategy <steam_community_market.requests.exponential_backoff_strategy>`.

        Raises
        ------
        IndexError
            Raised when ``app_id`` and ``market_hash_names`` have different lengths.
        TooManyRequestsException
            Raised when the request limit has been reached, after reaching the max retry limit, if any. Default retry limit is 5.
        TypeError
            Raised when any of the parameters are of the wrong type.

        Returns
        -------
        dict[str, dict[str, bool or float or int or str] or None]
            An overview of each item. Overview includes both volume and prices.
        """

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
                _request_overview(
                    id,
                    name,
                    currency or self.currency,
                    raise_exception=False,
                    rate_limit_handler=rate_limit_handler
                    or exponential_backoff_strategy,
                )
            ]
        }

    @typechecked
    @sanitized
    def get_overviews_from_dict(
        self,
        market_items_dict: dict[Union[AppID, int], list[str]],
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> dict[str, dict[str, Union[bool, float, int, str]]]:
        """Gets the prices and volumes of one or more items on the Steam Community Market from a dictionary.
        
        .. versionchanged:: 1.3.0
        
        Parameters
        ----------
        market_items_dict : dict[AppID or int, list[str]]
            A dictionary containing app IDs as `keys` and a list of item names as `value`.
        type_conversion : bool
            Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        currency : Currency or LegacyCurrency or int or str or None
            Currency used for prices. Defaults to the value imposed by the instance of the class.
        rate_limit_handler : Callable[[int], tuple[bool, float]] or None
            A function that handles the rate limit. It should take one parameter, the number of seconds to wait, and return a tuple containing a \
            :obj:`bool` indicating whether the request should be retried and the number of seconds to wait. Defaults to \
            :func:`exponential_backoff_strategy <steam_community_market.requests.exponential_backoff_strategy>`.

        Raises
        ------
        TooManyRequestsException
            Raised when the request limit has been reached, after reaching the max retry limit, if any. Default retry limit is 5.
        TypeError
            Raised when any of the parameters are of the wrong type.
            
        Returns
        -------
        dict[str, dict[str, bool or float or int or str]]
            An overview of each item. Overview includes both volume and prices.
        """

        result = {}
        for app_id, names in market_items_dict.items():
            for name in names:
                overview = _request_overview(
                    app_id,
                    name,
                    currency or self.currency,
                    raise_exception=False,
                    rate_limit_handler=rate_limit_handler
                    or exponential_backoff_strategy,
                )
                if type_conversion:
                    result[name] = self._overview_type_converter(overview)
                else:
                    result[name] = overview

        return result

    @typechecked
    @sanitized
    def get_price(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        price_type: str,
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
    ) -> Optional[float]:
        """Gets the lowest or median price of an item.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        app_id : AppID or int
            The app ID of the game the item is from.
        market_hash_name : str
            The name of the item; how it appears on the Steam Community Market.
        price_type : str
            The type of price. Can be either ``lowest_price`` or ``median_price``.
        type_conversion : bool
            Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        currency : Currency or LegacyCurrency or int or str or None
            Currency used for prices. Defaults to the value imposed by the instance of the class.

        Raises
        ------
        InvalidItemOrAppIDException
            Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        TooManyRequestsException
            Raised when the request limit has been reached.
        TypeError
            Raised when any of the parameters are of the wrong type.
        ValueError
            Raised when ``price_type`` is not one of ``lowest_price`` or ``median_price``.

        Returns
        -------
        float or None
            The price of the item, if suceess. :obj:`None` otherwise.
        """

        return self._get_price(
            app_id, market_hash_name, price_type, type_conversion, currency
        )

    @typechecked
    @sanitized
    def get_prices(
        self,
        app_id: Union[AppID, int, list[Union[AppID, int]]],
        market_hash_names: list[str],
        price_type: tuple[str, ...] = ("lowest_price", "median_price"),
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> dict[str, Optional[dict[str, Union[float, str]]]]:
        """Gets the lowest and/or median price of one or more items on the Steam Community Market, if they exist.

        .. versionchanged:: 1.3.0

        Parameters
        ----------
        app_id : AppID or int or list[AppID or int]
            If given a list, it needs to have the same length as ``market_hash_names``. If given :obj:`int` or \
            :class:`AppID <steam_community_market.enums.AppID>`, every item in ``market_hash_names`` must part of the same :class:`AppID <steam_community_market.enums>`.
        market_hash_names : list[str]
            A list of item names; how they appear on the Steam Community Market.
        price_type : tuple[str, ...]
            A tuple containing the types of price. Can be either ``lowest_price`` or ``median_price``. Defaults to both.
        type_conversion : bool
            Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        currency : Currency or LegacyCurrency or int or str or None
            Currency used for prices. Defaults to the value imposed by the instance of the class.
        rate_limit_handler : Callable[[int], tuple[bool, float]] or None
            A function that handles the rate limit. It should take one parameter, the number of seconds to wait, and return a tuple containing a \
            :obj:`bool` indicating whether the request should be retried and the number of seconds to wait. Defaults to \
            :func:`exponential_backoff_strategy <steam_community_market.requests.exponential_backoff_strategy>`.

        Raises
        ------
        IndexError
            Raised when ``app_id`` and ``market_hash_names`` have different lengths.
        TooManyRequestsException
            Raised when the request limit has been reached, after reaching the max retry limit, if any. Default retry limit is 5.
        TypeError
            Raised when any of the parameters are of the wrong type.
        ValueError
            Raised when ``price_type`` is not one of ``lowest_price`` or ``median_price`` or both.

        Returns
        -------
        dict[str, dict[str, float or str] or None]
            The lowest and/or median price of multiple items, if suceess. :obj:`None` otherwise.
        """

        if not isinstance(app_id, list):
            app_id = [app_id] * len(market_hash_names)

        if len(market_hash_names) != len(app_id):
            raise IndexError(
                'The length of "market_hash_names" and "app_id" must be the same.'
            )

        return {
            name: price
            for name, id in zip(market_hash_names, app_id)
            for price in [
                self._get_price(
                    id,
                    name,
                    price_type,
                    type_conversion,
                    currency,
                    False,
                    rate_limit_handler,
                )
            ]
        }

    @typechecked
    @sanitized
    def get_lowest_price(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
    ) -> Optional[float]:
        """Gets the lowest price of an item in the Steam Community Market, if is exists.

        .. versionchanged:: 1.3.0

        Parameters
        ----------
        app_id : AppID or int
            The app ID of the game the item is from.
        market_hash_name : str
            The name of the item; how it appears on the Steam Community Market.
        type_conversion : bool
            Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        currency : Currency or LegacyCurrency or int or str or None
            Currency used for prices. Defaults to the value imposed by the instance of the class.

        Raises
        ------
        InvalidItemOrAppIDException
            Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        TooManyRequestsException
            Raised when the request limit has been reached.
        TypeError
            Raised when any of the parameters are of the wrong type.

        Returns
        -------
        float or None
            The lowest price of the item, if suceess. :obj:`None` otherwise.
        """

        return self._get_price(
            app_id,
            market_hash_name,
            "lowest_price",
            type_conversion,
            currency or self.currency,
        )

    @typechecked
    @sanitized
    def get_median_price(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
    ) -> Optional[float]:
        """Gets the median price of an item in the Steam Community Market, if it exists.

        .. versionchanged:: 1.3.0

        Parameters
        ----------
        app_id : AppID or int
            The app ID of the game the item is from.
        market_hash_name : str
            The name of the item; how it appears on the Steam Community Market.
        type_conversion : bool
            Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
        currency : Currency or LegacyCurrency or int or str or None
            Currency used for prices. Defaults to the value imposed by the instance of the class.

        Raises
        ------
        InvalidItemOrAppIDException
            Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        TooManyRequestsException
            Raised when the request limit has been reached.
        TypeError
            Raised when any of the parameters are of the wrong type.

        Returns
        -------
        float or None
            The median price of the item, if suceess. :obj:`None` otherwise.
        """

        return self._get_price(
            app_id,
            market_hash_name,
            "median_price",
            type_conversion,
            currency or self.currency,
        )

    @typechecked
    @sanitized
    def get_volume(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
    ) -> Optional[int]:
        """Gets the volume of an item in the Steam Community Market, if it exists.

        .. versionchanged:: 1.3.0

        Parameters
        ----------
        app_id : AppID or int
            The app ID of the game the item is from.
        market_hash_name : str
            The name of the item; how it appears on the Steam Community Market.
        type_conversion : bool
            Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.

        Raises
        ------
        InvalidItemOrAppIDException
            Raised when the ``app_id`` or ``market_hash_name``, or the combination of both, is invalid.
        TooManyRequestsException
            Raised when the request limit has been reached.
        TypeError
            Raised when any of the parameters are of the wrong type.

        Returns
        -------
        int or None
            The volume of the item, if suceess. :obj:`None` otherwise.
        """

        item = _request_overview(app_id, market_hash_name, self.currency)
        if item is None or "volume" not in item:
            return None

        return (
            int(item["volume"].replace(",", "")) if type_conversion else item["volume"]
        )

    def _get_price(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        price_type: Union[str, tuple[str, ...]],
        type_conversion: bool = True,
        currency: Union[Currency, LegacyCurrency, int, str] = None,
        raise_exception: bool = True,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> Optional[Union[dict[str, Union[float, str]], float, str]]:
        item = _request_overview(
            app_id,
            market_hash_name,
            currency or self.currency,
            raise_exception,
            rate_limit_handler,
        )
        if item is None:
            return None

        if any(key not in item for key in price_type):
            return None

        if type_conversion:
            return {key: self._price_to_float(item[key]) for key in price_type}
        else:
            return {key: item[key] for key in price_type}

    @staticmethod
    def _overview_type_converter(
        overview: dict, keys_to_convert: list[str] = None
    ) -> dict[str, Union[str, int, float]]:
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
        if not (match := re.search(r"(\d{1,3}(?:[.,]\d{3})*)(?:[.,](\d{2}))?", value)):
            return None

        num_str = match[1].replace(",", "").replace(".", "")
        decimal_part = match[2] if match[2] is not None else "00"
        return float(f"{num_str}.{decimal_part}")
