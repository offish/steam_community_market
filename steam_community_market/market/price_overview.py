from ..currencies import Currency, LegacyCurrency
from ..decorators import sanitized, typechecked
from ..enums import AppID
from ..requests import _request_overview, exponential_backoff_strategy

from typing import Callable, Optional, Union

import re


class PriceOverview:
    """A class representing the cumulus of functionalities that are using the ``/market/priceoverview`` endpoint of the Steam Community Market API.

    Note
    ----
    This class is abstract and should not be instantiated directly, use :class:`Market <steam_community_market.market.instance.Market>` instead.
    """

    def __init__(self, currency: Currency):
        self.currency = currency

    def __new__(cls, currency: Currency):
        if cls is PriceOverview:
            raise TypeError(
                "PriceOverview is an abstract class and cannot be instantiated."
            )

        return super().__new__(cls)

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

        overview = _request_overview(
            app_id, market_hash_name, currency or self.currency  # type: ignore
        )
        if type_conversion:
            overview = self._overview_type_converter(overview)

        return overview

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
            A list containing the names of the items; how they appear on the Steam Community Market.
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

        return {
            market_hash_name: (
                self._overview_type_converter(overview) if type_conversion else overview
            )
            for id, market_hash_name in zip(app_id, market_hash_names)  # type: ignore
            for overview in [
                _request_overview(
                    id,
                    market_hash_name,
                    currency or self.currency,  # type: ignore
                    False,
                    rate_limit_handler or exponential_backoff_strategy,
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
            A dictionary containing the app IDs of the games the items are from as keys and a list of the names of the items; how they appear on the \
            Steam Community Market as values.
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

        return {
            market_hash_name: (
                self._overview_type_converter(overview) if type_conversion else overview
            )
            for app_id, market_hash_names in market_items_dict.items()
            for market_hash_name in market_hash_names
            for overview in [
                _request_overview(
                    app_id,
                    market_hash_name,
                    currency or self.currency,  # type: ignore
                    False,
                    rate_limit_handler or exponential_backoff_strategy,
                )
            ]
        }

    @typechecked
    @sanitized
    def get_price(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        price_type: str,
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
    ) -> Optional[Union[float, str]]:
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
        float or str or None
            The price of the item, if success. :obj:`None` otherwise.
        """

        return self._get_price(
            app_id,
            market_hash_name,
            (price_type,),
            type_conversion,
            currency or self.currency,
        )  # type: ignore

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
    ) -> dict[str, Optional[Union[dict[str, Optional[Union[float, str]]], float, str]]]:
        """Gets the lowest and/or median price of one or more items on the Steam Community Market, if they exist.

        .. versionchanged:: 1.3.0

        Parameters
        ----------
        app_id : AppID or int or list[AppID or int]
            If given a list, it needs to have the same length as ``market_hash_names``. If given :obj:`int` or \
            :class:`AppID <steam_community_market.enums.AppID>`, every item in ``market_hash_names`` must part of the same :class:`AppID <steam_community_market.enums>`.
        market_hash_names : list[str]
            A list containing the names of the items; how they appear on the Steam Community Market.
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
        dict[str, dict[str, float or str] or float or str or None]
            The lowest and/or median price of multiple items, if success. :obj:`None` otherwise.
        """

        return {
            f"{market_hash_name}": price
            for id, market_hash_name in zip(app_id, market_hash_names)  # type: ignore
            for price in [
                self._get_price(
                    id,
                    market_hash_name,
                    price_type,
                    type_conversion,
                    currency,
                    False,
                    rate_limit_handler or exponential_backoff_strategy,
                )
            ]
        }

    @typechecked
    @sanitized
    def get_prices_from_dict(
        self,
        market_items_dict: dict[Union[AppID, int], list[str]],
        price_type: tuple[str, ...] = ("lowest_price", "median_price"),
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> dict[str, Optional[Union[dict[str, Optional[Union[float, str]]], float, str]]]:
        """Gets the lowest and/or median price of one or more items on the Steam Community Market from a dictionary.
        
        .. versionadded:: 1.3.0
        
        Parameters
        ----------
        market_items_dict : dict[AppID or int, list[str]]
            A dictionary containing the app IDs of the games the items are from as keys and a list of the names of the items; how they appear on the \
            Steam Community Market as values.
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
        TooManyRequestsException
            Raised when the request limit has been reached, after reaching the max retry limit, if any. Default retry limit is 5.
        TypeError
            Raised when any of the parameters are of the wrong type.
        ValueError
            Raised when ``price_type`` is not one of ``lowest_price`` or ``median_price`` or both.
            
        Returns
        -------
        dict[str, dict[str, float or str] or float or str or None]
            The lowest and/or median price of multiple items, if success. :obj:`None` otherwise.
        """

        return {
            market_hash_name: self._get_price(
                app_id,
                market_hash_name,
                price_type,
                type_conversion,
                currency,
                False,
                rate_limit_handler or exponential_backoff_strategy,
            )
            for app_id, market_hash_names in market_items_dict.items()
            for market_hash_name in market_hash_names
        }

    @typechecked
    @sanitized
    def get_lowest_price(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
    ) -> Optional[Union[float, str]]:
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
            The lowest price of the item, if success. :obj:`None` otherwise.
        """

        return self._get_price(
            app_id,
            market_hash_name,
            ("lowest_price",),
            type_conversion,
            currency or self.currency,
        )  # type: ignore

    @typechecked
    @sanitized
    def get_lowest_prices(
        self,
        app_id: Union[AppID, int, list[Union[AppID, int]]],
        market_hash_names: list[str],
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> dict[str, Optional[Union[float, str]]]:
        """Gets the lowest price of one or more items on the Steam Community Market, if they exist.
        
        .. versionadded:: 1.3.0
        
        Parameters
        ----------
        app_id : AppID or int or list[AppID or int]
            The app ID of the game the item is from.
        market_hash_names : list[str]
            A list containing the names of the items; how they appear on the Steam Community Market.
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
        dict[str, float or str or None]
            The lowest price of multiple items, if success. :obj:`None` otherwise.
        """

        return {
            f"{market_hash_name}": price
            for id, market_hash_name in zip(app_id, market_hash_names)  # type: ignore
            for price in [
                self._get_price(
                    id,
                    market_hash_name,
                    ("lowest_price",),
                    type_conversion,
                    currency,
                    False,
                    rate_limit_handler or exponential_backoff_strategy,
                )
            ]
        }

    @typechecked
    @sanitized
    def get_lowest_prices_from_dict(
        self,
        market_items_dict: dict[Union[AppID, int], list[str]],
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> dict[str, Optional[Union[float, str]]]:
        """Gets the lowest price of one or more items on the Steam Community Market from a dictionary.
        
        .. versionadded:: 1.3.0
        
        Parameters
        ----------
        market_items_dict : dict[AppID or int, list[str]]
            A dictionary containing the app IDs of the games the items are from as keys and a list of the names of the items; how they appear on the \
            Steam Community Market as values.
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
        dict[str, float or str or None]
            The lowest price of multiple items, if success. :obj:`None` otherwise.
        """

        return {
            market_hash_name: self._get_price(
                app_id,
                market_hash_name,
                ("lowest_price",),
                type_conversion,
                currency,
                False,
                rate_limit_handler or exponential_backoff_strategy,
            )
            for app_id, market_hash_names in market_items_dict.items()
            for market_hash_name in market_hash_names
        }  # type: ignore

    @typechecked
    @sanitized
    def get_median_price(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
    ) -> Optional[Union[float, str]]:
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
            The median price of the item, if success. :obj:`None` otherwise.
        """

        return self._get_price(
            app_id,
            market_hash_name,
            ("median_price",),
            type_conversion,
            currency or self.currency,
        )  # type: ignore

    @typechecked
    @sanitized
    def get_median_prices(
        self,
        app_id: Union[AppID, int, list[Union[AppID, int]]],
        market_hash_names: list[str],
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> dict[str, Optional[Union[float, str]]]:
        """Gets the median price of one or more items on the Steam Community Market, if they exist.
        
        .. versionadded:: 1.3.0
        
        Parameters
        ----------
        app_id : AppID or int or list[AppID or int]
            The app ID of the game the item is from.
        market_hash_names : list[str]
            A list containing the names of the items; how they appear on the Steam Community Market.
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
        dict[str, float or str or None]
            The median price of multiple items, if success. :obj:`None` otherwise.
        """

        return {
            f"{market_hash_name}": price
            for id, market_hash_name in zip(app_id, market_hash_names)  # type: ignore
            for price in [
                self._get_price(
                    id,
                    market_hash_name,
                    ("median_price",),
                    type_conversion,
                    currency,
                    False,
                    rate_limit_handler or exponential_backoff_strategy,
                )
            ]
        }

    @typechecked
    @sanitized
    def get_median_prices_from_dict(
        self,
        market_items_dict: dict[Union[AppID, int], list[str]],
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> dict[str, Optional[Union[float, str]]]:
        """Gets the median price of one or more items on the Steam Community Market from a dictionary.
        
        .. versionadded:: 1.3.0
        
        Parameters
        ----------
        market_items_dict : dict[AppID or int, list[str]]
            A dictionary containing the app IDs of the games the items are from as keys and a list of the names of the items; how they appear on the \
            Steam Community Market as values.
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
        dict[str, float or str or None]
            The median price of multiple items, if success. :obj:`None` otherwise.
        """

        return {
            market_hash_name: self._get_price(
                app_id,
                market_hash_name,
                ("median_price",),
                type_conversion,
                currency,
                False,
                rate_limit_handler or exponential_backoff_strategy,
            )
            for app_id, market_hash_names in market_items_dict.items()
            for market_hash_name in market_hash_names
        }  # type: ignore

    @typechecked
    @sanitized
    def get_volume(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
    ) -> Optional[Union[int, str]]:
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
        int or str or None
            The volume of the item, if success. :obj:`None` otherwise.
        """

        return self._get_volume(app_id, market_hash_name, type_conversion)

    @typechecked
    @sanitized
    def get_volumes(
        self,
        app_id: Union[AppID, int, list[Union[AppID, int]]],
        market_hash_names: list[str],
        type_conversion: bool = True,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> dict[str, Optional[Union[int, str]]]:
        """Gets the volume of one or more items on the Steam Community Market, if they exist.
        
        .. versionchanged:: 1.3.0
        
        Parameters
        ----------
        app_id : AppID or int or list[AppID or int]
            The app ID of the game the item is from.
        market_hash_names : list[str]
            A list containing the names of the items; how they appear on the Steam Community Market.
        type_conversion : bool
            Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
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
        dict[str, int or str or None]
            The volume of multiple items, if success. :obj:`None` otherwise.
        """

        return {
            f"{market_hash_name}": volume
            for id, market_hash_name in zip(app_id, market_hash_names)  # type: ignore
            for volume in [
                self._get_volume(
                    id,
                    market_hash_name,
                    type_conversion,
                    False,
                    rate_limit_handler or exponential_backoff_strategy,
                )
            ]
        }

    @typechecked
    @sanitized
    def get_volumes_from_dict(
        self,
        market_items_dict: dict[Union[AppID, int], list[str]],
        type_conversion: bool = True,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> dict[str, Optional[Union[int, str]]]:
        """Gets the median price of one or more items on the Steam Community Market from a dictionary.
        
        .. versionadded:: 1.3.0
        
        Parameters
        ----------
        market_items_dict : dict[AppID or int, list[str]]
            A dictionary containing the app IDs of the games the items are from as keys and a list of the names of the items; how they appear on the \
            Steam Community Market as values.
        type_conversion : bool
            Whether to convert the returned values to their corresponding types. Defaults to :obj:`True`.
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
        dict[str, float or str or None]
            The median price of multiple items, if success. :obj:`None` otherwise.
        """

        return {
            market_hash_name: self._get_volume(
                app_id,
                market_hash_name,
                type_conversion,
                False,
                rate_limit_handler or exponential_backoff_strategy,
            )
            for app_id, market_hash_names in market_items_dict.items()
            for market_hash_name in market_hash_names
        }

    def _get_price(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        price_type: tuple[str, ...],
        type_conversion: bool = True,
        currency: Optional[Union[Currency, LegacyCurrency, int, str]] = None,
        raise_exception: bool = True,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> Optional[Union[dict[str, Union[float, str]], float, str]]:
        item = _request_overview(
            app_id,
            market_hash_name,
            currency or self.currency,  # type: ignore
            raise_exception,
            rate_limit_handler,
        )
        if item is None:
            return None

        convert = self._price_to_float if type_conversion else lambda x: x
        result = {}
        for key in price_type:
            price = item.get(key)
            result[key] = convert(price) if price is not None else price  # type: ignore

        return result if len(price_type) > 1 else result[price_type[0]]

    def _get_volume(
        self,
        app_id: Union[AppID, int],
        market_hash_name: str,
        type_conversion: bool = True,
        raise_exception: bool = True,
        rate_limit_handler: Optional[Callable[[int], tuple[bool, float]]] = None,
    ) -> Optional[Union[int, str]]:
        overview = _request_overview(
            app_id, market_hash_name, self.currency, raise_exception, rate_limit_handler
        )
        if overview is None or "volume" not in overview:
            return None

        return (
            int(overview["volume"].replace(",", "")) if type_conversion else overview["volume"]  # type: ignore
        )

    @staticmethod
    def _overview_type_converter(
        overview: dict, keys_to_convert: Optional[list[str]] = None
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
                result[key] = PriceOverview._price_to_float(value)
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
