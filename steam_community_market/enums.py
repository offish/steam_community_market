from enum import IntEnum


class AppID(IntEnum):
    """A short list of Steam apps that have a community market.

    .. list-table:: Steam Apps with Community Market
       :header-rows: 1

       * - App ID
         - App Name
       * - 440
         - Team Fortress 2
       * - 570
         - Dota 2
       * - 730
         - Counter-Strike: Global Offensive
       * - 753
         - Steam
       * - 219740
         - Don't Starve
       * - 232090
         - Killing Floor 2
       * - 250820
         - SteamVR
       * - 304930
         - Unturned
       * - 322330
         - Don't Starve Together
       * - 578080
         - PUBG: PlayerUnknown's Battlegrounds
       * - 252490
         - Rust
    """

    #: Team Fortress 2
    TF2 = 440

    #: Dota 2
    DOTA2 = 570

    #: Counter-Strike: Global Offensive
    CSGO = 730

    #: Steam
    STEAM = 753

    #: Don't Starve
    DS = 219740

    #: Killing Floor 2
    KF2 = 232090

    #: SteamVR
    STEAMVR = 250820

    #: Unturned
    UNTURNED = 304930

    #: Don't Starve Together
    DST = 322330

    #: PUBG: PlayerUnknown's Battlegrounds
    PUBG = 578080

    #: Rust
    RUST = 252490
