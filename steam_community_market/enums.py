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

    :ivar native_name: The native name of the language.
    :vartype native_name: str
    :ivar english_name: The English name of the language.
    :vartype english_name: str
    :ivar code: The language code of the language.
    :vartype code: str
    """

    native_name: str
    english_name: str
    code: str

    ARABIC = ("العربية", "arabic", "ar")
    """The Arabic language.
    
    :ivar native_name: ``العربية``
    :vartype native_name: str
    :ivar english_name: ``arabic``
    :vartype english_name: str
    :ivar code: ``ar``
    :vartype code: str
    """

    BULGARIAN = ("български език", "bulgarian", "bg")
    """The Bulgarian language.
    
    :ivar native_name: ``български език``
    :vartype native_name: str
    :ivar english_name: ``bulgarian``
    :vartype english_name: str
    :ivar code: ``bg``
    :vartype code: str
    """

    CHINESE_SIMPLIFIED = ("简体中文", "schinese", "zh-CN")
    """The Chinese (Simplified) language.
    
    :ivar native_name: ``简体中文``
    :vartype native_name: str
    :ivar english_name: ``schinese``
    :vartype english_name: str
    :ivar code: ``zh-CN``
    :vartype code: str
    """

    CHINESE_TRADITIONAL = ("繁體中文", "tchinese", "zh-TW")
    """The Chinese (Traditional) language.
    
    :ivar native_name: ``繁體中文``
    :vartype native_name: str
    :ivar english_name: ``tchinese``
    :vartype english_name: str
    :ivar code: ``zh-TW``
    :vartype code: str
    """

    CZECH = ("čeština", "czech", "cs")
    """The Czech language.
    
    :ivar native_name: ``čeština``
    :vartype native_name: str
    :ivar english_name: ``czech``
    :vartype english_name: str
    :ivar code: ``cs``
    :vartype code: str
    """

    DANISH = ("Dansk", "danish", "da")
    """The Danish language.
    
    :ivar native_name: ``Dansk``
    :vartype native_name: str
    :ivar english_name: ``danish``
    :vartype english_name: str
    :ivar code: ``da``
    :vartype code: str
    """

    DUTCH = ("Nederlands", "dutch", "nl")
    """The Dutch language.
    
    :ivar native_name: ``Nederlands``
    :vartype native_name: str
    :ivar english_name: ``dutch``
    :vartype english_name: str
    :ivar code: ``nl``
    :vartype code: str
    """

    ENGLISH = ("English", "english", "en")
    """The English language.
    
    :ivar native_name: ``English``
    :vartype native_name: str
    :ivar english_name: ``english``
    :vartype english_name: str
    :ivar code: ``en``
    :vartype code: str
    """

    FINNISH = ("Suomi", "finnish", "fi")
    """The Finnish language.
    
    :ivar native_name: ``Suomi``
    :vartype native_name: str
    :ivar english_name: ``finnish``
    :vartype english_name: str
    :ivar code: ``fi``
    :vartype code: str
    """

    FRENCH = ("Français", "french", "fr")
    """The French language.
    
    :ivar native_name: ``Français``
    :vartype native_name: str
    :ivar english_name: ``french``
    :vartype english_name: str
    :ivar code: ``fr``
    :vartype code: str
    """

    GERMAN = ("Deutsch", "german", "de")
    """The German language.
    
    :ivar native_name: ``Deutsch``
    :vartype native_name: str
    :ivar english_name: ``german``
    :vartype english_name: str
    :ivar code: ``de``
    :vartype code: str
    """

    GREEK = ("Ελληνικά", "greek", "el")
    """The Greek language.
    
    :ivar native_name: ``Ελληνικά``
    :vartype native_name: str
    :ivar english_name: ``greek``
    :vartype english_name: str
    :ivar code: ``el``
    :vartype code: str
    """

    HUNGARIAN = ("Magyar", "hungarian", "hu")
    """The Hungarian language.
    
    :ivar native_name: ``Magyar``
    :vartype native_name: str
    :ivar english_name: ``hungarian``
    :vartype english_name: str
    :ivar code: ``hu``
    :vartype code: str
    """

    ITALIAN = ("Italiano", "italian", "it")
    """The Italian language.
    
    :ivar native_name: ``Italiano``
    :vartype native_name: str
    :ivar english_name: ``italian``
    :vartype english_name: str
    :ivar code: ``it``
    :vartype code: str
    """

    JAPANESE = ("日本語", "japanese", "ja")
    """The Japanese language.
    
    :ivar native_name: ``日本語``
    :vartype native_name: str
    :ivar english_name: ``japanese``
    :vartype english_name: str
    :ivar code: ``ja``
    :vartype code: str
    """

    KOREAN = ("한국어", "koreana", "ko")
    """The Korean language.
    
    :ivar native_name: ``한국어``
    :vartype native_name: str
    :ivar english_name: ``koreana``
    :vartype english_name: str
    :ivar code: ``ko``
    :vartype code: str
    """

    NORWEGIAN = ("Norsk", "norwegian", "no")
    """The Norwegian language.
    
    :ivar native_name: ``Norsk``
    :vartype native_name: str
    :ivar english_name: ``norwegian``
    :vartype english_name: str
    :ivar code: ``no``
    :vartype code: str
    """

    POLISH = ("Polski", "polish", "pl")
    """The Polish language.
    
    :ivar native_name: ``Polski``
    :vartype native_name: str
    :ivar english_name: ``polish``
    :vartype english_name: str
    :ivar code: ``pl``
    :vartype code: str
    """

    PORTUGUESE = ("Português", "portuguese", "pt")
    """The Portuguese language.
    
    :ivar native_name: ``Português``
    :vartype native_name: str
    :ivar english_name: ``portuguese``
    :vartype english_name: str
    :ivar code: ``pt``
    :vartype code: str
    """

    PORTUGUESE_BRAZIL = ("Português-Brasil", "brazilian", "pt-BR")
    """The Brazilian Portuguese language.
    
    :ivar native_name: ``Português-Brasil``
    :vartype native_name: str
    :ivar english_name: ``brazilian``
    :vartype english_name: str
    :ivar code: ``pt-BR``
    :vartype code: str
    """

    ROMANIAN = ("Română", "romanian", "ro")
    """The Romanian language.
    
    :ivar native_name: ``Română``
    :vartype native_name: str
    :ivar english_name: ``romanian``
    :vartype english_name: str
    :ivar code: ``ro``
    :vartype code: str
    """

    RUSSIAN = ("Русский", "russian", "ru")
    """The Russian language.
    
    :ivar native_name: ``Русский``
    :vartype native_name: str
    :ivar english_name: ``russian``
    :vartype english_name: str
    :ivar code: ``ru``
    :vartype code: str
    """

    SPANISH_SPAIN = ("Español-España", "spanish", "es")
    """The Spanish language.
    
    :ivar native_name: ``Español-España``
    :vartype native_name: str
    :ivar english_name: ``spanish``
    :vartype english_name: str
    :ivar code: ``es``
    :vartype code: str
    """

    SPANISH_LATIN_AMERICA = ("Español-Latinoamérica", "latam", "es-419")
    """The Latin American Spanish language.
    
    :ivar native_name: ``Español-Latinoamérica``
    :vartype native_name: str
    :ivar english_name: ``latam``
    :vartype english_name: str
    :ivar code: ``es-419``
    :vartype code: str
    """

    SWEDISH = ("Svenska", "swedish", "sv")
    """The Swedish language.
    
    :ivar native_name: ``Svenska``
    :vartype native_name: str
    :ivar english_name: ``swedish``
    :vartype english_name: str
    :ivar code: ``sv``
    :vartype code: str
    """

    THAI = ("ไทย", "thai", "th")
    """The Thai language.
    
    :ivar native_name: ``ไทย``
    :vartype native_name: str
    :ivar english_name: ``thai``
    :vartype english_name: str
    :ivar code: ``th``
    :vartype code: str
    """

    TURKISH = ("Türkçe", "turkish", "tr")
    """The Turkish language.
    
    :ivar native_name: ``Türkçe``
    :vartype native_name: str
    :ivar english_name: ``turkish``
    :vartype english_name: str
    :ivar code: ``tr``
    :vartype code: str
    """

    UKRAINIAN = ("Українська", "ukrainian", "uk")
    """The Ukrainian language.
    
    :ivar native_name: ``Українська``
    :vartype native_name: str
    :ivar english_name: ``ukrainian``
    :vartype english_name: str
    :ivar code: ``uk``
    :vartype code: str
    """

    VIETNAMESE = ("Tiếng Việt", "vietnamese", "vn")
    """The Vietnamese language.
    
    :ivar native_name: ``Tiếng Việt``
    :vartype native_name: str
    :ivar english_name: ``vietnamese``
    :vartype english_name: str
    :ivar code: ``vn``
    :vartype code: str
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

        :param language: The language to get in string form.
        :type language: str
        :return: The language object, or :obj:`None` if the language was not found.
        :rtype: Language or None
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
