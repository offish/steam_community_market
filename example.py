from steam_community_market import Market, ESteamCurrency, AppID


market = Market(ESteamCurrency.NOK) # Could either be: 'NOK', 'nok' or 9.
# For USD; leave it empty or use 'USD', 'usd' or 1.


# get_overview
# Example using get_overview
market.get_overview("Mann Co. Supply Crate Key", AppID.TF2)
# {'success': True, 'lowest_price': '22,12 kr', 'volume': '6,489', 'median_price': '21,75 kr'}


# get_lowest_price
# Example using get_lowest_price
market.get_lowest_price("Weapon Barrel", AppID.RUST)
# 69.01


# get_median_price
# Example using get_median_price
market.get_median_price("No Mercy AK47", 252490)  # 252490 is Rust's AppID
# 43.3


# get_volume
# Example using get_volume
# Getting Steam items is kind of weird, you need to look at it's URL.
# IDF (CSGO Trading Card), you need to add 730- to. So it would be "730-IDF".
market.get_volume("753-Sack of Gems", AppID.STEAM)
# 4739


# get_prices
# Example using get_prices
market.get_prices("Mann Co. Supply Crate Key", 440) # 440 is TF2's AppID
# {'lowest_price': 24.04, 'median_price': 23.81}


# get_overviews_from_dict
# Example using get_overviews_from_dict.
items = {
    "Mann Co. Supply Crate Key": {
        "appid": 440
    },
    "AK-47 | Redline (Field-Tested)": {
        "appid": 730
    } # Do not add a comma at the end of the last entry.
}

market.get_overviews_from_dict(items)
# {'Mann Co. Supply Crate Key': {'success': True, 'lowest_price': '22,36 kr', 'volume': '6,489', 'median_price': '21,75 kr'}, 
#   'AK-47 | Redline (Field-Tested)': {'success': True, 'lowest_price': '136,51 kr', 'volume': '749', 'median_price': '131,36 kr'}}
