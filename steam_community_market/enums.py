import enum


class ESteamSupportedCurrency(enum.IntEnum):
    #: United States Dollar
    USD = 1

    #: Great Britain Pound
    GBP = 2

    #: Euro
    EUR = 3

    #: Swiss Franc
    CHF = 4

    #: Russian Ruble
    RUB = 5

    #: Polish Złoty
    PLN = 6

    #: Brazilian Real
    BRL = 7

    #: Japanese Yen
    JPY = 8

    #: Norwegian Krone
    NOK = 9

    #: Indonesian Rupiah
    IDR = 10

    #: Malaysian Ringgit
    MYR = 11

    #: Philippine Peso
    PHP = 12

    #: Singapore Dollar
    SGD = 13

    #: Thai Baht
    THB = 14

    #: Vietnamese Dong
    VND = 15

    #: South Korean Won
    KRW = 16

    #: Turkish Lira
    TRY = 17

    #: Ukrainian Hryvnia
    UAH = 18

    #: Mexican Peso
    MXN = 19

    #: Canadian Dollar
    CAD = 20

    #: Australian Dollar
    AUD = 21

    #: New Zealand Dollar
    NZD = 22

    #: Chinese Yuan
    CNY = 23

    #: Indian Rupee
    INR = 24

    #: Chilean Peso
    CLP = 25

    #: Peruvian Sol
    PEN = 26

    #: Colombian Peso
    COP = 27

    #: South African Rand
    ZAR = 28

    #: Hong Kong Dollar
    HKD = 29

    #: New Taiwan Dollar
    TWD = 30

    #: Saudi Riyal
    SAR = 31

    #: United Arab Emirates Dirham
    AED = 32

    #: Argentine Peso
    ARS = 34

    #: Israeli New Sheqel
    ILS = 35

    #: Kazakhstani Tenge
    KZT = 37

    #: Kuwaiti Dinar
    KWD = 38

    #: Qatari Rial
    QAR = 39

    #: Costa Rican Colón
    CRC = 40

    #: Uruguayan Peso
    UYU = 41

    # Expanding mechanism


class ESteamUnsupportedCurrency(enum.IntEnum):
    #: Swedish Krona
    SEK = 33

    #: Belarusian Ruble
    BYN = 36

    #: Bulgarian Lev
    BGN = 42

    #: Croatian Kuna
    HRK = 43

    #: Czech Koruna
    CZK = 44

    #: Danish Krone
    DKK = 45

    #: Hungarian Forint
    HUF = 46

    #: Romanian Leu
    RON = 47


class ESteamCurrency(enum.IntEnum):
    locals().update(ESteamSupportedCurrency.__members__)
    locals().update(ESteamUnsupportedCurrency.__members__)


class AppID(enum.IntEnum):
    TF2 = 440
    DOTA2 = 570
    CSGO = 730
    STEAM = 753
    RUST = 252490
