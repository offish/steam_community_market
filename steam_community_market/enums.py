from enum import IntEnum


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
