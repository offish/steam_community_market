from steam_community_market.market import Market



market = Market('NOK') # Could either be: 'NOK', 'nok' or 9.
# For USD; leave it empty or use 'USD', 'usd' or 1.
# For all the currencies supported go here: 
# https://github.com/offish/steam_community_market/blob/master/steam_community_market/market.py#L5



# Example using get_price.
# First parameter is the name of the item how it appears on the Steam Community Market.
# Second parameter is the AppID of the game the item is from.
market.get_price('Mann Co. Supply Crate Key', 440) # 440 is TF2's AppID.
# >>> {'success': True, 'lowest_price': '22,12 kr', 'volume': '6,489', 'median_price': '21,75 kr'}



# Example using get_prices with the same AppID.
items = ['Mann Co. Supply Crate Key', 'Tour of Duty Ticket']
market.get_prices(items, 440) 
# >>> {'Mann Co. Supply Crate Key': {'success': True, 'lowest_price': '22,36 kr', 'volume': '6,489', 'median_price': '21,75 kr'}, 
#       'Tour of Duty Ticket': {'success': True, 'lowest_price': '9,21 kr', 'volume': '668', 'median_price': '9,61 kr'}}



# Example using get_prices with different AppIDs.
items = ['Mann Co. Supply Crate Key', 'AWP | Atheris (Field-Tested)']
appids = [440, 730] # 440 is TF2, 730 is CSGO. 
# These two lists MUST have the same length. In this case they both have 2 elements.
market.get_prices(items, appids)
# >>> {'Mann Co. Supply Crate Key': {'success': True, 'lowest_price': '22,01 kr', 'volume': '6,489', 'median_price': '21,75 kr'}, 
#       'AWP | Atheris (Field-Tested)': {'success': True, 'lowest_price': '47,68 kr', 'volume': '1,381', 'median_price': '45,39 kr'}}



# Example using get_prices_from_dict.
items = {
    "Mann Co. Supply Crate Key": {
        "appid": 440
    },
    "AK-47 | Redline (Field-Tested)": {
        "appid": 730
    } # Do not add a comma at the end of the last entry.
}

market.get_prices_from_dict(items)
# >>> {'Mann Co. Supply Crate Key': {'success': True, 'lowest_price': '22,36 kr', 'volume': '6,489', 'median_price': '21,75 kr'}, 
#       'AK-47 | Redline (Field-Tested)': {'success': True, 'lowest_price': '136,51 kr', 'volume': '749', 'median_price': '131,36 kr'}}
