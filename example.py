import json
import os

from steam_community_market import (
    AppID,
    InvalidItemOrAppIDException,
    Market,
    Currency,
)


# Because we love "Mann Co. Supply Crate Key" <3
MANN_CO_SUPPLY_CRATE_KEY = "Mann Co. Supply Crate Key"

# Could either be: "Euro", "EUR" or 3.
# For "USD"; leave it empty or use Currency.USD, "United States Dollar", "USD" or 1.
market = Market(Currency.EUR)


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
#   "success": true,
#   "lowest_price": 2.1,
#   "volume": 24675,
#   "median_price": 2.1
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
#     "lowest_price": 2.1,
#     "volume": 24675,
#     "median_price": 2.1
#   },
#   "Name Tag": {
#     "success": true,
#     "lowest_price": 0.46,
#     "volume": 726,
#     "median_price": 0.45
#   },
#   "The Festivizer": {
#     "success": true,
#     "lowest_price": 1.24,
#     "volume": 336,
#     "median_price": 1.07
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
#     "lowest_price": 2.1,
#     "volume": 24675,
#     "median_price": 2.1
#   },
#   "AK-47 | Redline (Field-Tested)": {
#     "success": true,
#     "lowest_price": 21.77,
#     "volume": 399,
#     "median_price": 21.8
#   },
#   "Wood": {
#     "success": true,
#     "lowest_price": 0.32,
#     "volume": 816,
#     "median_price": 0.3
#   }
# }

# get_overviews_from_dict
market_items_dict = {
    AppID.TF2: [MANN_CO_SUPPLY_CRATE_KEY, "Name Tag", "The Festivizer"],
    730: ["AK-47 | Redline (Field-Tested)", "M4A4 | Howl (Field-Tested)"],
    252490: ["Weapon Stock", "Weapon Grip"],
}

print(
    "get_overviews_from_dict:",
    json.dumps(
        market.get_overviews_from_dict(market_items_dict), indent=2, ensure_ascii=False
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
#     "lowest_price": 2.1,
#     "volume": 24675,
#     "median_price": 2.1
#   },
#   "Name Tag": {
#     "success": true,
#     "lowest_price": 0.46,
#     "volume": 726,
#     "median_price": 0.45
#   },
#   "The Festivizer": {
#     "success": true,
#     "lowest_price": 1.24,
#     "volume": 336,
#     "median_price": 1.07
#   },
#   "AK-47 | Redline (Field-Tested)": {
#     "success": true,
#     "lowest_price": 21.77,
#     "volume": 399,
#     "median_price": 21.8
#   },
#   "M4A4 | Howl (Field-Tested)": {
#     "success": true
#   },
#   "Weapon Stock": {
#     "success": false
#   },
#   "Weapon Grip": {
#     "success": false
#   }
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
# 6.6


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
# 6.7
#
# get_price (median_price):
# 11.49

# get_prices (1)
market_hash_names = [MANN_CO_SUPPLY_CRATE_KEY, "Name Tag", "The Festivizer"]

print(
    "get_prices (1):",
    json.dumps(
        market.get_prices(AppID.TF2, market_hash_names),
        indent=2,
        ensure_ascii=False,
    ),
    sep=os.linesep,
    end=os.linesep * 2,
)
# get_prices (1):
# {
#   "Mann Co. Supply Crate Key": {
#     "lowest_price": 2.1,
#     "median_price": 2.1
#   },
#   "Name Tag": {
#     "lowest_price": 0.46,
#     "median_price": 0.45
#   },
#   "The Festivizer": {
#     "lowest_price": 1.24,
#     "median_price": 1.07
#   }
# }

# get_prices (2)
app_ids = [AppID.TF2, 730, AppID.RUST]
market_hash_names = [MANN_CO_SUPPLY_CRATE_KEY, "AK-47 | Redline (Field-Tested)", "Wood"]

print(
    "get_prices (2):",
    json.dumps(
        market.get_prices(app_ids, market_hash_names),
        indent=2,
        ensure_ascii=False,
    ),
    sep=os.linesep,
    end=os.linesep * 2,
)
# get_prices (2):
# {
#   "Mann Co. Supply Crate Key": {
#     "lowest_price": 2.1,
#     "median_price": 2.1
#   },
#   "AK-47 | Redline (Field-Tested)": {
#     "lowest_price": 21.77,
#     "median_price": 21.8
#   },
#   "Wood": {
#     "lowest_price": 0.32,
#     "median_price": 0.3
#   }
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
# 3430
