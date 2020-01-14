# steam_community_market
[![Version](https://img.shields.io/pypi/v/steam_community_market.svg)](https://pypi.org/project/steam_community_market/)
[![License](https://img.shields.io/github/license/offish/steam_community_market.svg)](https://github.com/offish/steam_community_market/blob/master/LICENSE.txt)
[![Stars](https://img.shields.io/github/stars/offish/steam_community_market.svg)](https://github.com/offish/steam_community_market/stargazers)
[![Issues](https://img.shields.io/github/issues/offish/steam_community_market.svg)](https://github.com/offish/steam_community_market/issues)
[![Size](https://img.shields.io/github/repo-size/offish/steam_community_market.svg)](https://pypi.org/project/steam-community-market/)
[![Discord](https://img.shields.io/discord/467040686982692865.svg)](https://discord.gg/t8nHSvA)
<br>
[![Steam Donate Button](https://img.shields.io/badge/donate-steam-green.svg)](https://steamcommunity.com/tradeoffer/new/?partner=293059984&token=0-l_idZR "Support this project via Steam")
[![PayPal Donate Button](https://img.shields.io/badge/donate-paypal-blue.svg)](https://www.paypal.me/0ffish "Support this project via PayPal")

Easily get item prices and volumes from the Steam Community Market using Python 3



Table of Content
================
* [Installation](https://github.com/offish/steam_community_market#Installation)
* [Usage](https://github.com/offish/steam_community_market#Usage)
* [Methods](https://github.com/offish/steam_community_market#Methods)
* [License](https://github.com/offish/steam_community_market#License)

Installation
============
```
pip install steam_community_market
```

Update
======
```
pip install --upgrade steam_commmunity_market
```

Usage
=====
```python
from steam_community_market.market import Market

market = Market('USD')
```
`'USD'` can either be `str`, `int` or empty. Find the currencies supported [here](https://github.com/offish/steam_community_market/blob/master/steam_community_market/market.py#L5).



Methods
=======
### Get one item:

**get_price(name: str, app_id: int)**

```python
>>> market.get_price('Prisma Case', 730)
{'success': True, 'lowest_price': '$0.41', 'volume': '59,613', 'median_price': '$0.41'}
```
`name`: The name of an item how it appears on the Steam Community Market.

`app_id`: The AppID of the item.

### Get multiple items with different AppIDs:

**get_prices(names: list, app_id: (int, list))**

```python
>>> items = ['Prisma Case', 'Danger Zone Case', 'Spectrum 10 Case']
>>> appids = [730, 730, 440]
>>> market.get_prices(items, appids)
{
    'Prisma Case': {
        'success': True, 
        'lowest_price': '$0.39', 
        'volume': '59,613', 
        'median_price': '$0.41'
    },

    'Danger Zone Case': {
        'success': True, 
        'lowest_price': '$0.20', 
        'volume': '56,664', 
        'median_price': '$0.22'
    },

    'Spectrum 10 Case': {
        'success': False
    }
}
```
`names`:  A list of items how each item name (market_hash_name) appears on the Steam Community Market.

`app_id`: A list of AppIDs.

### Get multiple items with the same AppID:

**get_prices(names: list, app_id: (int, list))**

```python
>>> items = ['Prisma Case', 'Danger Zone Case', 'Spectrum 10 Case']
>>> market.get_prices(items, 730)
{
    'Prisma Case': {
        'success': True, 
        'lowest_price': '$0.39', 
        'volume': '59,613', 
        'median_price': '$0.41'
    },

    'Danger Zone Case': {
        'success': True, 
        'lowest_price': '$0.20', 
        'volume': '56,664', 
        'median_price': '$0.22'
    },

    'Spectrum 10 Case': {
        'success': False
    }
}
```
`names`:  A list of items how each item name (market_hash_name) appears on the Steam Community Market.

`app_id`: The AppID of the items.

**All of the items listed in `names` must have the same `app_id`.**

### Get multiple items with different AppIDs from dict

**get_prices_from_dict(items: dict)**
```python
>>> items = {
        "Mann Co. Supply Crate Key": {
            "appid": 440
        },
        "AK-47 | Redline (Field-Tested)": {
            "appid": 730
        }
    }
>>> market.get_prices_from_dict(items)
{
    'Mann Co. Supply Crate Key': {
        'success': True, 
        'lowest_price': '$2.50', 
        'volume': '6,489', 
        'median_price': '$2.45'
    }, 
    'AK-47 | Redline (Field-Tested)': {
        'success': True, 
        'lowest_price': '$15.00', 
        'volume': '749', 
        'median_price': '$14.78'
    }
}
```


License
=======
MIT License

Copyright (c) 2020 [offish](mailto:overutilization@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
