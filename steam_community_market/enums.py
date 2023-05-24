from enum import Enum, IntEnum
from functools import lru_cache


class AppID(IntEnum):
    """A short, incomplete, list of Steam apps that have a community market."""

    TF2 = 440
    """The app ID of ``Team Fortress 2``."""

    DOTA2 = 570
    """The app ID of ``Dota 2``."""

    CSGO = 730
    """The app ID of ``Counter-Strike: Global Offensive``."""

    STEAM = 753
    """The app ID of ``Steam``."""

    DS = 219740
    """The app ID of ``Don't Starve``."""

    KF2 = 232090
    """The app ID of ``Killing Floor 2``."""

    STEAMVR = 250820
    """The app ID of ``SteamVR``."""

    UNTURNED = 304930
    """The app ID of ``Unturned``."""

    DST = 322330
    """The app ID of ``Don't Starve Together``."""

    PUBG = 578080
    """The app ID of ``PLAYERUNKNOWN'S BATTLEGROUNDS``."""

    RUST = 252490
    """The app ID of ``Rust``."""


class Language(Enum):
    """The list of all languages supported by the Steam Community Market, which includes their native name, English name, and language code.

    .. versionadded:: 1.3.0

    Attributes
    ----------
    native_name : str
        The native name of the language.
    english_name : str
        The English name of the language.
    code : str
        The language code of the language.
    """

    native_name: str
    english_name: str
    code: str

    ARABIC = ("العربية", "arabic", "ar")
    """The Arabic language.
    
    Attributes
    ----------
    native_name : str
        ``العربية``
    english_name : str
        ``arabic``
    code : str
        ``ar``
    """

    BULGARIAN = ("български език", "bulgarian", "bg")
    """The Bulgarian language.
    
    Attributes
    ----------
    native_name : str
        ``български език``
    english_name : str
        ``bulgarian``
    code : str
        ``bg``
    """

    CHINESE_SIMPLIFIED = ("简体中文", "schinese", "zh-CN")
    """The Chinese (Simplified) language.
    
    Attributes
    ----------
    native_name : str
        ``简体中文``
    english_name : str
        ``schinese``
    code : str
        ``zh-CN``
    """

    CHINESE_TRADITIONAL = ("繁體中文", "tchinese", "zh-TW")
    """The Chinese (Traditional) language.
    
    Attributes
    ----------
    native_name : str
        ``繁體中文``
    english_name : str
        ``tchinese``
    code : str
        ``zh-TW``
    """

    CZECH = ("čeština", "czech", "cs")
    """The Czech language.
    
    Attributes
    ----------
    native_name : str
        ``čeština``
    english_name : str
        ``czech``
    code : str
        ``cs``
    """

    DANISH = ("Dansk", "danish", "da")
    """The Danish language.
    
    Attributes
    ----------
    native_name : str
        ``Dansk``
    english_name : str
        ``danish``
    code : str
        ``da``
    """

    DUTCH = ("Nederlands", "dutch", "nl")
    """The Dutch language.
    
    Attributes
    ----------
    native_name : str
        ``Nederlands``
    english_name : str
        ``dutch``
    code : str
        ``nl``
    """

    ENGLISH = ("English", "english", "en")
    """The English language.
    
    Attributes
    ----------
    native_name : str
        ``English``
    english_name : str
        ``english``
    code : str
        ``en``
    """

    FINNISH = ("Suomi", "finnish", "fi")
    """The Finnish language.
    
    Attributes
    ----------
    native_name : str
        ``Suomi``
    english_name : str
        ``finnish``
    code : str
        ``fi``
    """

    FRENCH = ("Français", "french", "fr")
    """The French language.
    
    Attributes
    ----------
    native_name : str
        ``Français``
    english_name : str
        ``french``
    code : str
        ``fr``
    """

    GERMAN = ("Deutsch", "german", "de")
    """The German language.
    
    Attributes
    ----------
    native_name : str
        ``Deutsch``
    english_name : str
        ``german``
    code : str
        ``de``
    """

    GREEK = ("Ελληνικά", "greek", "el")
    """The Greek language.
    
    Attributes
    ----------
    native_name : str
        ``Ελληνικά``
    english_name : str
        ``greek``
    code : str
        ``el``
    """

    HUNGARIAN = ("Magyar", "hungarian", "hu")
    """The Hungarian language.
    
    Attributes
    ----------
    native_name : str
        ``Magyar``
    english_name : str
        ``hungarian``
    code : str
        ``hu``
    """

    ITALIAN = ("Italiano", "italian", "it")
    """The Italian language.
    
    Attributes
    ----------
    native_name : str
        ``Italiano``
    english_name : str
        ``italian``
    code : str
        ``it``
    """

    JAPANESE = ("日本語", "japanese", "ja")
    """The Japanese language.
    
    Attributes
    ----------
    native_name : str
        ``日本語``
    english_name : str
        ``japanese``
    code : str
        ``ja``
    """

    KOREAN = ("한국어", "koreana", "ko")
    """The Korean language.
    
    Attributes
    ----------
    native_name : str
        ``한국어``
    english_name : str
        ``koreana``
    code : str
        ``ko``
    """

    NORWEGIAN = ("Norsk", "norwegian", "no")
    """The Norwegian language.
    
    Attributes
    ----------
    native_name : str
        ``Norsk``
    english_name : str
        ``norwegian``
    code : str
        ``no``
    """

    POLISH = ("Polski", "polish", "pl")
    """The Polish language.
    
    Attributes
    ----------
    native_name : str
        ``Polski``
    english_name : str
        ``polish``
    code : str
        ``pl``
    """

    PORTUGUESE = ("Português", "portuguese", "pt")
    """The Portuguese language.
    
    Attributes
    ----------
    native_name : str
        ``Português``
    english_name : str
        ``portuguese``
    code : str
        ``pt``
    """

    PORTUGUESE_BRAZIL = ("Português-Brasil", "brazilian", "pt-BR")
    """The Brazilian Portuguese language.
    
    Attributes
    ----------
    native_name : str
        ``Português-Brasil``
    english_name : str
        ``brazilian``
    code : str
        ``pt-BR``
    """

    ROMANIAN = ("Română", "romanian", "ro")
    """The Romanian language.
    
    Attributes
    ----------
    native_name : str
        ``Română``
    english_name : str
        ``romanian``
    code : str
        ``ro``
    """

    RUSSIAN = ("Русский", "russian", "ru")
    """The Russian language.
    
    Attributes
    ----------
    native_name : str
        ``Русский``
    english_name : str
        ``russian``
    code : str
        ``ru``
    """

    SPANISH_SPAIN = ("Español-España", "spanish", "es")
    """The Spanish language.
    
    Attributes
    ----------
    native_name : str
        ``Español-España``
    english_name : str
        ``spanish``
    code : str
        ``es``
    """

    SPANISH_LATIN_AMERICA = ("Español-Latinoamérica", "latam", "es-419")
    """The Latin American Spanish language.
    
    Attributes
    ----------
    native_name : str
        ``Español-Latinoamérica``
    english_name : str
        ``latam``
    code : str
        ``es-419``
    """

    SWEDISH = ("Svenska", "swedish", "sv")
    """The Swedish language.
    
    Attributes
    ----------
    native_name : str
        ``Svenska``
    english_name : str
        ``swedish``
    code : str
        ``sv``
    """

    THAI = ("ไทย", "thai", "th")
    """The Thai language.
    
    Attributes
    ----------
    native_name : str
        ``ไทย``
    english_name : str
        ``thai``
    code : str
        ``th``
    """

    TURKISH = ("Türkçe", "turkish", "tr")
    """The Turkish language.
    
    Attributes
    ----------
    native_name : str
        ``Türkçe``
    english_name : str
        ``turkish``
    code : str
        ``tr``
    """

    UKRAINIAN = ("Українська", "ukrainian", "uk")
    """The Ukrainian language.
    
    Attributes
    ----------
    native_name : str
        ``Українська``
    english_name : str
        ``ukrainian``
    code : str
        ``uk``
    """

    VIETNAMESE = ("Tiếng Việt", "vietnamese", "vn")
    """The Vietnamese language.
    
    Attributes
    ----------
    native_name : str
        ``Tiếng Việt``
    english_name : str
        ``vietnamese``
    code : str
        ``vn``
    """

    def __new__(cls, native_name: str, english_name: str, code: str):
        obj = object.__new__(cls)
        obj._value_ = (native_name, english_name, code)
        obj.native_name = native_name
        obj.english_name = english_name
        obj.code = code
        return obj

    @classmethod
    @lru_cache(maxsize=None)
    def from_string(cls, language: str):
        """Get a language from a string. The string can be the language's object name, native name, English name, or language code.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        language : str
            The language to get in string form.

        Returns
        -------
        Language or None
            The language object, or None if the language was not found.
        """

        if not hasattr(cls, "_lookup"):
            cls._lookup = {
                key.upper(): steam_lang
                for steam_lang in cls
                for key in (
                    steam_lang.name.replace("_", " "),
                    steam_lang.native_name,
                    steam_lang.english_name,
                    steam_lang.code,
                )
            }

        return cls._lookup.get(language.upper())
