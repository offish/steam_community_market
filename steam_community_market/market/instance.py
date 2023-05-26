from ..currencies import Currency, LegacyCurrency
from ..decorators import sanitized, typechecked
from ..enums import Language

from .price_overview import PriceOverview

from typing import Union


class Market(PriceOverview):
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

    @typechecked
    @sanitized
    def __init__(
        self,
        currency: Union[Currency, LegacyCurrency, int, str] = Currency.USD,
        # language: Union[Language, str] = Language.ENGLISH,
    ) -> None:
        super().__init__(currency)  # type: ignore
        self.currency: Currency = currency  # type: ignore
        # self.language: Language = language  # type: ignore
