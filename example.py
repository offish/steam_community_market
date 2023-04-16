import json
import os

from steam_community_market import (
    AppID,
    InvalidItemOrAppIDException,
    Market,
    SteamCurrency,
)


# Because we love "Mann Co. Supply Crate Key" <3
MANN_CO_SUPPLY_CRATE_KEY = "Mann Co. Supply Crate Key"

# Could either be: 'EUR', 'eur' or 3.
# For USD; leave it empty or use SteamCurrency.USD, 'USD', 'usd' or 1.
market = Market(SteamCurrency.EUR)


# get_overview
print(
    "get_overview:",
    json.dumps(
        market.get_overview(AppID.TF2, MANN_CO_SUPPLY_CRATE_KEY),
        indent=2,
        ensure_ascii=False,
    ),
    sep=os.linesep,
    end=os.linesep * 2,
)
# get_overview:
# {
#   'success': True,
#   'lowest_price': '2,22€',
#   'volume': '18,015',
#   'median_price': '2,25€'
# }


# get_overviews (1)
market_hash_names = [MANN_CO_SUPPLY_CRATE_KEY, "Name Tag", "The Festivizer"]
print(
    "get_overviews (1):",
    json.dumps(
        market.get_overviews(AppID.TF2, market_hash_names),
        indent=2,
        ensure_ascii=False,
    ),
    sep=os.linesep,
    end=os.linesep * 2,
)
# get_overviews (1):
# {
#   "Mann Co. Supply Crate Key": {
#     "success": true,
#     "lowest_price": "2,24€",
#     "volume": "18,015",
#     "median_price": "2,25€"
#   },
#   "Name Tag": {
#     "success": true,
#     "lowest_price": "0,37€",
#     "volume": "1,114",
#     "median_price": "0,38€"
#   },
#   "The Festivizer": {
#     "success": true,
#     "lowest_price": "1,26€",
#     "volume": "510",
#     "median_price": "1,25€"
#   }
# }

# get_overviews (2)
app_ids = [AppID.TF2, 730, AppID.RUST]
market_hash_names = [MANN_CO_SUPPLY_CRATE_KEY, "AK-47 | Redline (Field-Tested)", "Wood"]
print(
    "get_overviews (2):",
    json.dumps(
        market.get_overviews(app_ids, market_hash_names),
        indent=2,
        ensure_ascii=False,
    ),
    sep=os.linesep,
    end=os.linesep * 2,
)
# get_overviews (2):
# {
#   "Mann Co. Supply Crate Key": {
#     "success": true,
#     "lowest_price": "2,23€",
#     "volume": "18,015",
#     "median_price": "2,25€"
#   },
#   "AK-47 | Redline (Field-Tested)": {
#     "success": true,
#     "lowest_price": "23,77€",
#     "volume": "447",
#     "median_price": "23,03€"
#   },
#   "Wood": {
#     "success": true,
#     "lowest_price": "0,35€",
#     "volume": "1,329",
#     "median_price": "0,34€"
#   }
# }

# get_overviews_from_dict
market_hash_names = {
    AppID.TF2: [MANN_CO_SUPPLY_CRATE_KEY, "Name Tag", "The Festivizer"],
    730: ["AK-47 | Redline (Field-Tested)", "M4A4 | Howl (Field-Tested)"],
    252490: ["Weapon Stock", "Weapon Grip"],
}

print(
    "get_overviews_from_dict:",
    json.dumps(
        market.get_overviews_from_dict(market_hash_names), indent=2, ensure_ascii=False
    ),
    sep=os.linesep,
    end=os.linesep * 2,
)
# 730 - CS:GO's App ID
# 252490 - Rust's App ID
# get_overviews_from_dict:
# {
#   "Mann Co. Supply Crate Key": {
#     "success": true,
#     "lowest_price": "2,25€",
#     "volume": "18,015",
#     "median_price": "2,25€"
#   },
#   "Name Tag": {
#     "success": true,
#     "lowest_price": "0,38€",
#     "volume": "1,114",
#     "median_price": "0,38€"
#   },
#   "The Festivizer": {
#     "success": true,
#     "lowest_price": "1,26€",
#     "volume": "510",
#     "median_price": "1,25€"
#   },
#   "AK-47 | Redline (Field-Tested)": {
#     "success": true,
#     "lowest_price": "23,--€",
#     "volume": "447",
#     "median_price": "23,03€"
#   },
#   "M4A4 | Howl (Field-Tested)": {
#     "success": true
#   },
#   "Weapon Stock": null,
#   "Weapon Grip": null
# }

# get_lowest_price (get_price) - Exception
try:
    print(
        "get_lowest_price:",
        market.get_lowest_price(AppID.CSGO, "Weapon Barrel"),
        sep=os.linesep,
        end=os.linesep * 2,
    )
except InvalidItemOrAppIDException as e:
    print(
        "[InvalidItemOrAppIDException] get_lowest_price:",
        e,
        sep=os.linesep,
        end=os.linesep * 2,
    )

print(
    "get_price (lowest_price):",
    market.get_price(252490, "No Mercy AK47", "lowest_price"),
    sep=os.linesep,
    end=os.linesep * 2,
)
# 252490 - Rust's App ID
# [InvalidItemOrAppIDException] get_lowest_price:
# Item "Weapon Barrel" with app ID "730" is considered invalid by the Steam Community Market.
#
# get_price (lowest_price):
# 6.33


# get_median_price (get_price)
print(
    "get_median_price:",
    market.get_median_price(252490, "No Mercy AK47"),
    sep=os.linesep,
    end=os.linesep * 2,
)
print(
    "get_price (median_price):",
    market.get_price(AppID.RUST, "Weapon Barrel", "median_price"),
    sep=os.linesep,
    end=os.linesep * 2,
)
# 252490 - Rust's App ID
# get_median_price:
# 6.33
#
# get_price (median_price):
# 12.26


# get_prices
print(
    "get_prices:",
    json.dumps(
        market.get_prices(440, MANN_CO_SUPPLY_CRATE_KEY), indent=2, ensure_ascii=False
    ),
    sep=os.linesep,
    end=os.linesep * 2,
)
# 440 - Team Fortress 2's App ID
# get_prices:
# {
#   'lowest_price': 2.22,
#   'median_price': 2.25
# }

# get_volume
# Getting information about "Steam" items is kind of weird, you need to look at its URL.
# IDF (CSGO Trading Card), you need to add 730- to. So it would be "730-IDF".
print(
    "get_volume:",
    market.get_volume(AppID.STEAM, "753-Sack of Gems"),
    sep=os.linesep,
    end=os.linesep * 2,
)
# get_volume:
# 4982
