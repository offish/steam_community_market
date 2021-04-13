from steam_community_market import Market, ESteamCurrency, AppID


market = Market(ESteamCurrency.NOK) # Could either be: 'NOK', 'nok' or 9.
# For USD; leave it empty or use ESteamCurrency.USD, 'USD', 'usd' or 1.


# get_overview
# Example using get_overview
print(market.get_overview("Mann Co. Supply Crate Key", AppID.TF2))
# {'success': True, 'lowest_price': '23,93 kr', 'volume': '7,608', 'median_price': '23,50 kr'}

# get_lowest_price
# Example using get_lowest_price
print(market.get_lowest_price("Weapon Barrel", AppID.RUST))
# 67.06


# get_median_price
# Example using get_median_price
print(market.get_median_price("No Mercy AK47", 252490))  # 252490 is Rust's AppID
# 41.04


# get_volume
# Example using get_volume
# Getting Steam items is kind of weird, you need to look at it's URL.
# IDF (CSGO Trading Card), you need to add 730- to. So it would be "730-IDF".
print(market.get_volume("753-Sack of Gems", AppID.STEAM))
# 4541


# get_prices
# Example using get_prices
print(market.get_prices("Mann Co. Supply Crate Key", 440)) # 440 is TF2's AppID
# {'lowest_price': 23.93, 'median_price': 23.5}


# get_overviews_from_dict
# Example using get_overviews_from_dict
items = {
    "Mann Co. Supply Crate Key": {
        "appid": 440
    },
    "AK-47 | Redline (Field-Tested)": {
        "appid": 730
    }
}

print(market.get_overviews_from_dict(items))
# {'Mann Co. Supply Crate Key': {'success': True, 'lowest_price': '23,93 kr', 'volume': '7,608', 'median_price': '23,50 kr'}, 
# 'AK-47 | Redline (Field-Tested)': {'success': True, 'lowest_price': '153,56 kr', 'volume': '890', 'median_price': '155,33 kr'}}
