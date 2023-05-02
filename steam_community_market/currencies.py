from enum import IntEnum
from functools import lru_cache


class Currency(IntEnum):
    """All currencies that have been supported by Steam at some point in time, including the ones found inside :class:`LegacyCurrency`.

    .. versionchanged:: 1.3.0

    :ivar english_name: The English name of the currency.
    :vartype english_name: str
    """

    english_name: str

    USD = (1, "United States Dollar")
    """The United States Dollar currency.
    
    :ivar english_name: ```United States Dollar```
    :vartype english_name: str
    """

    GBP = (2, "Great Britain Pound")
    """The Great Britain Pound currency.
    
    :ivar english_name: ```Great Britain Pound```
    :vartype english_name: str
    """

    EUR = (3, "Euro")
    """The Euro currency.
    
    :ivar english_name: ```Euro```
    :vartype english_name: str
    """

    CHF = (4, "Swiss Franc")
    """The Swiss Franc currency.
    
    :ivar english_name: ```Swiss Franc```
    :vartype english_name: str
    """

    RUB = (5, "Russian Ruble")
    """The Russian Ruble currency.
    
    :ivar english_name: ```Russian Ruble```
    :vartype english_name: str
    """

    PLN = (6, "Polish Złoty")
    """The Polish Złoty currency.
    
    :ivar english_name: ```Polish Złoty```
    :vartype english_name: str
    """

    BRL = (7, "Brazilian Real")
    """The Brazilian Real currency.
    
    :ivar english_name: ```Brazilian Real```
    :vartype english_name: str
    """

    JPY = (8, "Japanese Yen")
    """The Japanese Yen currency.
    
    :ivar english_name: ```Japanese Yen```
    :vartype english_name: str
    """

    NOK = (9, "Norwegian Krone")
    """The Norwegian Krone currency.
    
    :ivar english_name: ```Norwegian Krone```
    :vartype english_name: str
    """

    IDR = (10, "Indonesian Rupiah")
    """The Indonesian Rupiah currency.
    
    :ivar english_name: ```Indonesian Rupiah```
    :vartype english_name: str
    """

    MYR = (11, "Malaysian Ringgit")
    """The Malaysian Ringgit currency.
    
    :ivar english_name: ```Malaysian Ringgit```
    :vartype english_name: str
    """

    PHP = (12, "Philippine Peso")
    """The Philippine Peso currency.
    
    :ivar english_name: ```Philippine Peso```
    :vartype english_name: str
    """

    SGD = (13, "Singapore Dollar")
    """The Singapore Dollar currency.
    
    :ivar english_name: ```Singapore Dollar```
    :vartype english_name: str
    """

    THB = (14, "Thai Baht")
    """The Thai Baht currency.
    
    :ivar english_name: ```Thai Baht```
    :vartype english_name: str
    """

    VND = (15, "Vietnamese Dong")
    """The Vietnamese Dong currency.
    
    :ivar english_name: ```Vietnamese Dong```
    :vartype english_name: str
    """

    KRW = (16, "South Korean Won")
    """The South Korean Won currency.
    
    :ivar english_name: ```South Korean Won```
    :vartype english_name: str
    """

    TRY = (17, "Turkish Lira")
    """The Turkish Lira currency.
    
    :ivar english_name: ```Turkish Lira```
    :vartype english_name: str
    """

    UAH = (18, "Ukrainian Hryvnia")
    """The Ukrainian Hryvnia currency.
    
    :ivar english_name: ```Ukrainian Hryvnia```
    :vartype english_name: str
    """

    MXN = (19, "Mexican Peso")
    """The Mexican Peso currency.
    
    :ivar english_name: ```Mexican Peso```
    :vartype english_name: str
    """

    CAD = (20, "Canadian Dollar")
    """The Australian Dollar currency.
    
    :ivar english_name: ```Canadian Dollar```
    :vartype english_name: str
    """

    AUD = (21, "Australian Dollar")
    """The Australian Dollar currency.
    
    :ivar english_name: ```Australian Dollar```
    :vartype english_name: str
    """

    NZD = (22, "New Zealand Dollar")
    """The New Zealand Dollar currency.
    
    :ivar english_name: ```New Zealand Dollar```
    :vartype english_name: str
    """

    CNY = (23, "Chinese Yuan")
    """The Chinese Yuan currency.
    
    :ivar english_name: ```Chinese Yuan```
    :vartype english_name: str
    """

    INR = (24, "Indian Rupee")
    """The Indian Rupee currency.
    
    :ivar english_name: ```Indian Rupee```
    :vartype english_name: str
    """

    CLP = (25, "Chilean Peso")
    """The Chilean Peso currency.
    
    :ivar english_name: ```Chilean Peso```
    :vartype english_name: str
    """

    PEN = (26, "Peruvian Sol")
    """The Peruvian Sol currency.
    
    :ivar english_name: ```Peruvian Sol```
    :vartype english_name: str
    """

    COP = (27, "Colombian Peso")
    """The Colombian Peso currency.
    
    :ivar english_name: ```Colombian Peso```
    :vartype english_name: str
    """

    ZAR = (28, "South African Rand")
    """The South African Rand currency.
    
    :ivar english_name: ```South African Rand```
    :vartype english_name: str
    """

    HKD = (29, "Hong Kong Dollar")
    """The Hong Kong Dollar currency.
    
    :ivar english_name: ```Hong Kong Dollar```
    :vartype english_name: str
    """

    TWD = (30, "New Taiwan Dollar")
    """The New Taiwan Dollar currency.
    
    :ivar english_name: ```New Taiwan Dollar```
    :vartype english_name: str
    """

    SAR = (31, "Saudi Riyal")
    """The Saudi Riyal currency.
    
    :ivar english_name: ```Saudi Riyal```
    :vartype english_name: str
    """

    AED = (32, "United Arab Emirates Dirham")
    """The United Arab Emirates Dirham currency.
    
    :ivar english_name: ```United Arab Emirates Dirham```
    :vartype english_name: str
    """

    SEK = (33, "Swedish Krona")
    """The Swedish Krona currency.
    
    :ivar english_name: ```Swedish Krona```
    :vartype english_name: str
    """

    ARS = (34, "Argentine Peso")
    """The Argentine Peso currency.
    
    :ivar english_name: ```Argentine Peso```
    :vartype english_name: str
    """

    ILS = (35, "Israeli New Sheqel")
    """The Israeli New Sheqel currency.
    
    :ivar english_name: ```Israeli New Sheqel```
    :vartype english_name: str
    """

    BYN = (36, "Belarusian Ruble")
    """The Belarusian Ruble currency.
    
    :ivar english_name: ```Belarusian Ruble```
    :vartype english_name: str
    """

    KZT = (37, "Kazakhstani Tenge")
    """The Kazakhstani Tenge currency.
    
    :ivar english_name: ```Kazakhstani Tenge```
    :vartype english_name: str
    """

    KWD = (38, "Kuwaiti Dinar")
    """The Kuwaiti Dinar currency.
    
    :ivar english_name: ```Kuwaiti Dinar```
    :vartype english_name: str
    """

    QAR = (39, "Qatari Rial")
    """The Qatari Rial currency.
    
    :ivar english_name: ```Qatari Rial```
    :vartype english_name: str
    """

    CRC = (40, "Costa Rican Colón")
    """The Costa Rican Colón currency.
    
    :ivar english_name: ``Costa Rican Colón``
    :vartype english_name: str
    """

    UYU = (41, "Uruguayan Peso")
    """The Uruguayan Peso currency.
    
    :ivar english_name: ``Uruguayan Peso``
    :vartype english_name: str
    """

    BGN = (42, "Bulgarian Lev")
    """The Bulgarian Lev currency.
    
    :ivar english_name: ``Bulgarian Lev``
    :vartype english_name: str
    """

    HRK = (43, "Croatian Kuna")
    """The Croatian Kuna currency.
    
    :ivar english_name: ``Croatian Kuna``
    :vartype english_name: str
    """

    CZK = (44, "Czech Koruna")
    """The Czech Koruna currency.
    
    :ivar english_name: ``Czech Koruna``
    :vartype english_name: str
    """

    DKK = (45, "Danish Krone")
    """The Danish Krone currency.

    :ivar english_name: ``Danish Krone``
    :vartype english_name: str
    """

    HUF = (46, "Hungarian Forint")
    """The Hungarian Forint currency.
    
    :ivar english_name: ``Hungarian Forint``
    :vartype english_name: str
    """

    RON = (47, "Romanian Leu")
    """The Romanian Leu currency.
    
    :ivar english_name: ``Romanian Leu``
    :vartype english_name: str
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

        :param currency: The currency to get in string form.
        :type currency: str
        :return: The currency object, or :obj:`None` if the currency was not found.
        :rtype: Currency or None
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

    :ivar english_name: The English name of the currency.
    :vartype english_name: str
    """

    english_name: str

    SEK = (33, "Swedish Krona")
    """The Swedish Krona currency.
    
    :ivar english_name: ``Swedish Krona``
    :vartype english_name: str
    """

    BYN = (36, "Belarusian Ruble")
    """The Belarusian Ruble currency.
    
    :ivar english_name: ``Belarusian Ruble``
    :vartype english_name: str
    """

    BGN = (42, "Bulgarian Lev")
    """The Bulgarian Lev currency.
    
    :ivar english_name: ``Bulgarian Lev``
    :vartype english_name: str
    """

    HRK = (43, "Croatian Kuna")
    """The Croatian Kuna currency.
    
    :ivar english_name: ``Croatian Kuna``
    :vartype english_name: str
    """

    CZK = (44, "Czech Koruna")
    """The Czech Koruna currency.
    
    :ivar english_name: ``Czech Koruna``
    :vartype english_name: str
    """

    DKK = (45, "Danish Krone")
    """The Danish Krone currency.
    
    :ivar english_name: ``Danish Krone``
    :vartype english_name: str
    """

    HUF = (46, "Hungarian Forint")
    """The Hungarian Forint currency.
    
    :ivar english_name: ``Hungarian Forint``
    :vartype english_name: str
    """

    RON = (47, "Romanian Leu")
    """The Romanian Leu currency.
    
    :ivar english_name: ``Romanian Leu``
    :vartype english_name: str
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

        :param currency: The legacy currency to get in string form.
        :type currency: str
        :return: The legacy currency object, or :obj:`None` if the currency was not found.
        :rtype: LegacyCurrency or None
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
