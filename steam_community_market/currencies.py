from enum import IntEnum
from functools import lru_cache


class Currency(IntEnum):
    """All currencies that have been supported by Steam at some point in time, including the ones found inside \
        :class:`LegacyCurrency`.

    .. versionchanged:: 1.3.0

    Attributes
    ----------
    english_name : str
        The English name of the currency.
    """

    english_name: str

    USD = (1, "United States Dollar")
    """The United States Dollar currency.
    
    Attributes
    ----------
    english_name : str
        ``United States Dollar``
    """

    GBP = (2, "Great Britain Pound")
    """The Great Britain Pound currency.
    
    Attributes
    ----------
    english_name : str
        ``Great Britain Pound``
    """

    EUR = (3, "Euro")
    """The Euro currency.
    
    Attributes
    ----------
    english_name : str
        ``Euro``
    """

    CHF = (4, "Swiss Franc")
    """The Swiss Franc currency.
    
    Attributes
    ----------
    english_name : str
        ``Swiss Franc``
    """

    RUB = (5, "Russian Ruble")
    """The Russian Ruble currency.
    
    Attributes
    ----------
    english_name : str
        ``Russian Ruble``
    """

    PLN = (6, "Polish Złoty")
    """The Polish Złoty currency.
    
    Attributes
    ----------
    english_name : str
        ``Polish Złoty``
    """

    BRL = (7, "Brazilian Real")
    """The Brazilian Real currency.
    
    Attributes
    ----------
    english_name : str
        ``Brazilian Real``
    """

    JPY = (8, "Japanese Yen")
    """The Japanese Yen currency.
    
    Attributes
    ----------
    english_name : str
        ``Japanese Yen``
    """

    NOK = (9, "Norwegian Krone")
    """The Norwegian Krone currency.
    
    Attributes
    ----------
    english_name : str
        ``Norwegian Krone``
    """

    IDR = (10, "Indonesian Rupiah")
    """The Indonesian Rupiah currency.
    
    Attributes
    ----------
    english_name : str
        ``Indonesian Rupiah``
    """

    MYR = (11, "Malaysian Ringgit")
    """The Malaysian Ringgit currency.
    
    Attributes
    ----------
    english_name : str
        ``Malaysian Ringgit``
    """

    PHP = (12, "Philippine Peso")
    """The Philippine Peso currency.
    
    Attributes
    ----------
    english_name : str
        ``Philippine Peso``
    """

    SGD = (13, "Singapore Dollar")
    """The Singapore Dollar currency.
    
    Attributes
    ----------
    english_name : str
        ``Singapore Dollar``
    """

    THB = (14, "Thai Baht")
    """The Thai Baht currency.
    
    Attributes
    ----------
    english_name : str
        ``Thai Baht``
    """

    VND = (15, "Vietnamese Dong")
    """The Vietnamese Dong currency.
    
    Attributes
    ----------
    english_name : str
        ``Vietnamese Dong``
    """

    KRW = (16, "South Korean Won")
    """The South Korean Won currency.
    
    Attributes
    ----------
    english_name : str
        ``South Korean Won``
    """

    TRY = (17, "Turkish Lira")
    """The Turkish Lira currency.
    
    Attributes
    ----------
    english_name : str
        ``Turkish Lira``
    """

    UAH = (18, "Ukrainian Hryvnia")
    """The Ukrainian Hryvnia currency.
    
    Attributes
    ----------
    english_name : str
        ``Ukrainian Hryvnia``
    """

    MXN = (19, "Mexican Peso")
    """The Mexican Peso currency.
    
    Attributes
    ----------
    english_name : str
        ``Mexican Peso``
    """

    CAD = (20, "Canadian Dollar")
    """The Australian Dollar currency.
    
    Attributes
    ----------
    english_name : str
        ``Canadian Dollar``
    """

    AUD = (21, "Australian Dollar")
    """The Australian Dollar currency.
    
    Attributes
    ----------
    english_name : str
        ``Australian Dollar``
    """

    NZD = (22, "New Zealand Dollar")
    """The New Zealand Dollar currency.
    
    Attributes
    ----------
    english_name : str
        ``New Zealand Dollar``
    """

    CNY = (23, "Chinese Yuan")
    """The Chinese Yuan currency.
    
    Attributes
    ----------
    english_name : str
        ``Chinese Yuan``
    """

    INR = (24, "Indian Rupee")
    """The Indian Rupee currency.
    
    Attributes
    ----------
    english_name : str
        ``Indian Rupee``
    """

    CLP = (25, "Chilean Peso")
    """The Chilean Peso currency.
    
    Attributes
    ----------
    english_name : str
        ``Chilean Peso``
    """

    PEN = (26, "Peruvian Sol")
    """The Peruvian Sol currency.
    
    Attributes
    ----------
    english_name : str
        ``Peruvian Sol``
    """

    COP = (27, "Colombian Peso")
    """The Colombian Peso currency.
    
    Attributes
    ----------
    english_name : str
        ``Colombian Peso``
    """

    ZAR = (28, "South African Rand")
    """The South African Rand currency.
    
    Attributes
    ----------
    english_name : str
        ``South African Rand``
    """

    HKD = (29, "Hong Kong Dollar")
    """The Hong Kong Dollar currency.
    
    Attributes
    ----------
    english_name : str
        ``Hong Kong Dollar``
    """

    TWD = (30, "New Taiwan Dollar")
    """The New Taiwan Dollar currency.
    
    Attributes
    ----------
    english_name : str
        ``New Taiwan Dollar``
    """

    SAR = (31, "Saudi Riyal")
    """The Saudi Riyal currency.
    
    Attributes
    ----------
    english_name : str
        ``Saudi Riyal``
    """

    AED = (32, "United Arab Emirates Dirham")
    """The United Arab Emirates Dirham currency.
    
    Attributes
    ----------
    english_name : str
        ``United Arab Emirates Dirham``
    """

    SEK = (33, "Swedish Krona")
    """The Swedish Krona currency.
    
    Attributes
    ----------
    english_name : str
        ``Swedish Krona``
    """

    ARS = (34, "Argentine Peso")
    """The Argentine Peso currency.
    
    Attributes
    ----------
    english_name : str
        ``Argentine Peso``
    """

    ILS = (35, "Israeli New Sheqel")
    """The Israeli New Sheqel currency.
    
    Attributes
    ----------
    english_name : str
        ``Israeli New Sheqel``
    """

    BYN = (36, "Belarusian Ruble")
    """The Belarusian Ruble currency.
    
    Attributes
    ----------
    english_name : str
        ``Belarusian Ruble``
    """

    KZT = (37, "Kazakhstani Tenge")
    """The Kazakhstani Tenge currency.
    
    Attributes
    ----------
    english_name : str
        ``Kazakhstani Tenge``
    """

    KWD = (38, "Kuwaiti Dinar")
    """The Kuwaiti Dinar currency.
    
    Attributes
    ----------
    english_name : str
        ``Kuwaiti Dinar``
    """

    QAR = (39, "Qatari Rial")
    """The Qatari Rial currency.
    
    Attributes
    ----------
    english_name : str
        ``Qatari Rial``
    """

    CRC = (40, "Costa Rican Colón")
    """The Costa Rican Colón currency.
    
    Attributes
    ----------
    english_name : str
        ``Costa Rican Colón``
    """

    UYU = (41, "Uruguayan Peso")
    """The Uruguayan Peso currency.
    
    Attributes
    ----------
    english_name : str
        ``Uruguayan Peso``
    """

    BGN = (42, "Bulgarian Lev")
    """The Bulgarian Lev currency.
    
    Attributes
    ----------
    english_name : str
        ``Bulgarian Lev``
    """

    HRK = (43, "Croatian Kuna")
    """The Croatian Kuna currency.
    
    Attributes
    ----------
    english_name : str
        ``Croatian Kuna``
    """

    CZK = (44, "Czech Koruna")
    """The Czech Koruna currency.
    
    Attributes
    ----------
    english_name : str
        ``Czech Koruna``
    """

    DKK = (45, "Danish Krone")
    """The Danish Krone currency.

    Attributes
    ----------
    english_name : str
        ``Danish Krone``
    """

    HUF = (46, "Hungarian Forint")
    """The Hungarian Forint currency.
    
    Attributes
    ----------
    english_name : str
        ``Hungarian Forint``
    """

    RON = (47, "Romanian Leu")
    """The Romanian Leu currency.
    
    Attributes
    ----------
    english_name : str
        ``Romanian Leu``
    """

    def __new__(cls, value: int, english_name: str):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.english_name = english_name
        return obj

    @classmethod
    @lru_cache(maxsize=None)
    def from_string(cls, currency: str):
        """Get a currency from a string. The string can be the currencies English name or ISO 4217 code.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        currency : str
            The currency to get in string form.

        Returns
        -------
        Currency or None
            The currency object, or :obj:`None` if the currency was not found.
        """

        if not hasattr(cls, "_lookup"):
            cls._lookup = {
                key.upper(): curr
                for curr in cls
                for key in (
                    curr.name,
                    curr.english_name,
                )
            }

        return cls._lookup.get(currency.upper())


class LegacyCurrency(IntEnum):
    """Legacy currencies that have been supported by Steam, at some point in time, but are not any longer.

    .. versionadded:: 1.3.0

    Attributes
    ----------
    english_name : str
        The English name of the currency.
    """

    english_name: str

    SEK = (33, "Swedish Krona")
    """The Swedish Krona currency.
    
    Attributes
    ----------
    english_name : str
        ``Swedish Krona``
    """

    BYN = (36, "Belarusian Ruble")
    """The Belarusian Ruble currency.
    
    Attributes
    ----------
    english_name : str
        ``Belarusian Ruble``
    """

    BGN = (42, "Bulgarian Lev")
    """The Bulgarian Lev currency.
    
    Attributes
    ----------
    english_name : str
        ``Bulgarian Lev``
    """

    HRK = (43, "Croatian Kuna")
    """The Croatian Kuna currency.
    
    Attributes
    ----------
    english_name : str
        ``Croatian Kuna``
    """

    CZK = (44, "Czech Koruna")
    """The Czech Koruna currency.
    
    Attributes
    ----------
    english_name : str
        ``Czech Koruna``
    """

    DKK = (45, "Danish Krone")
    """The Danish Krone currency.
    
    Attributes
    ----------
    english_name : str
        ``Danish Krone``
    """

    HUF = (46, "Hungarian Forint")
    """The Hungarian Forint currency.
    
    Attributes
    ----------
    english_name : str
        ``Hungarian Forint``
    """

    RON = (47, "Romanian Leu")
    """The Romanian Leu currency.
    
    Attributes
    ----------
    english_name : str
        ``Romanian Leu``
    """

    def __new__(cls, value: int, english_name: str):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.english_name = english_name
        return obj

    @classmethod
    @lru_cache(maxsize=None)
    def from_string(cls, currency: str):
        """Get a legacy currency from a string. The string can be the currencies English name or ISO 4217 code.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        currency : str
            The legacy currency to get in string form.

        Returns
        -------
        LegacyCurrency or None
            The legacy currency object, or :obj:`None` if the currency was not found.
        """

        if not hasattr(cls, "_lookup"):
            cls._lookup = {
                key.upper(): legacy_curr
                for legacy_curr in cls
                for key in (
                    legacy_curr.name,
                    legacy_curr.english_name,
                )
            }

        return cls._lookup.get(currency.upper())
