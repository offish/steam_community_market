from enum import Enum, IntEnum, unique


class AppID(IntEnum):
    """A short, incomplete, list of Steam apps that have a community market."""

    #: ``Team Fortress 2``
    TF2 = 440

    #: ``Dota 2``
    DOTA2 = 570

    #: ``Counter-Strike: Global Offensive``
    CSGO = 730

    #: ``Steam``
    STEAM = 753

    #: ``Don't Starve``
    DS = 219740

    #: ``Killing Floor 2``
    KF2 = 232090

    #: ``SteamVR``
    STEAMVR = 250820

    #: ``Unturned``
    UNTURNED = 304930

    #: ``Don't Starve Together``
    DST = 322330

    #: ``PUBG: PlayerUnknown's Battlegrounds``
    PUBG = 578080

    #: ``Rust``
    RUST = 252490


@unique
class SteamLanguage(Enum):
    """The list of all languages supported by the Steam Community Market, which includes their native name, English name, and language code.

    :param native_name: The native name of the language.
    :type native_name: str
    :param english_name: The English name of the language.
    :type english_name: str
    :param language_code: The language code of the language.
    :type language_code: str

    .. versionadded:: 1.3.0
    """

    ARABIC = ("العربية", "arabic", "ar")
    BULGARIAN = ("български език", "bulgarian", "bg")
    CHINESE_SIMPLIFIED = ("简体中文", "schinese", "zh-CN")
    CHINESE_TRADITIONAL = ("繁體中文", "tchinese", "zh-TW")
    CZECH = ("čeština", "czech", "cs")
    DANISH = ("Dansk", "danish", "da")
    DUTCH = ("Nederlands", "dutch", "nl")
    ENGLISH = ("English", "english", "en")
    FINNISH = ("Suomi", "finnish", "fi")
    FRENCH = ("Français", "french", "fr")
    GERMAN = ("Deutsch", "german", "de")
    GREEK = ("Ελληνικά", "greek", "el")
    HUNGARIAN = ("Magyar", "hungarian", "hu")
    ITALIAN = ("Italiano", "italian", "it")
    JAPANESE = ("日本語", "japanese", "ja")
    KOREAN = ("한국어", "koreana", "ko")
    NORWEGIAN = ("Norsk", "norwegian", "no")
    POLISH = ("Polski", "polish", "pl")
    PORTUGUESE = ("Português", "portuguese", "pt")
    PORTUGUESE_BRAZIL = ("Português-Brasil", "brazilian", "pt-BR")
    ROMANIAN = ("Română", "romanian", "ro")
    RUSSIAN = ("Русский", "russian", "ru")
    SPANISH_SPAIN = ("Español-España", "spanish", "es")
    SPANISH_LATIN_AMERICA = ("Español-Latinoamérica", "latam", "es-419")
    SWEDISH = ("Svenska", "swedish", "sv")
    THAI = ("ไทย", "thai", "th")
    TURKISH = ("Türkçe", "turkish", "tr")
    UKRAINIAN = ("Українська", "ukrainian", "uk")
    VIETNAMESE = ("Tiếng Việt", "vietnamese", "vn")

    def __init__(self, native_name: str, english_name: str, code: str) -> None:
        self.native_name = native_name
        self.english_name = english_name
        self.code = code

    @classmethod
    def from_string(cls, language: str):
        """Get a language from a string. The string can be the language's object name, native name, English name, or language code.

        :param language: The language to get in string form.
        :type language: str
        :return: The language object, or :obj:`None` if the language was not found.
        :rtype: SteamLanguage or None

        .. versionadded:: 1.3.0
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

        language = language.upper()
        return cls._lookup.get(language)
