# steam-community-market

A synchronous Python read-only wrapper for the Steam Community Market API.

[![Version](https://img.shields.io/pypi/v/steam-community-market?color=0067a3&label=Version&logo=pypi&logoColor=0067a3)](https://pypi.org/project/steam-community-market/)
[![Supported Versions](https://img.shields.io/pypi/pyversions/steam-community-market?color=0067a3&label=Supported%20Versions&logo=pypi&logoColor=0067a3)](https://pypi.org/project/steam-community-market/)
[![License](https://img.shields.io/pypi/l/steam-community-market?color=0067a3&label=License&logo=pypi&logoColor=0067a3)](https://github.com/offish/steam-community-market/blob/master/LICENSE)
[![Documentation Status](https://img.shields.io/readthedocs/steam-community-market/latest?label=RTD&logo=read-the-docs&logoColor=ffffff)](https://steam-community-market.readthedocs.io/en/latest/)
[![GitHub Issues](https://img.shields.io/github/issues-raw/offish/steam_community_market?color=ffffff&label=Open%20Issues&logo=github)](https://github.com/offish/steam_community_market/issues)
[![GitHub Stars](https://img.shields.io/github/stars/offish/steam_community_market?color=ffffff&label=Stargazers&logo=github)](https://github.com/offish/steam_community_market/stargazers)
[![Discord](https://img.shields.io/discord/467040686982692865?color=7289da&label=Discord&logo=discord&logoColor=7289da)](https://discord.gg/t8nHSvA)

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Support](#support)
- [Contributing](#contributing)
- [Donations](#donations)
- [License](#license)

## Introduction

`steam-community-market` is a [Python](https://www.python.org/) library that provides a simple and efficient way to interact with the [Steam Community Market](https://steamcommunity.com/market/) API. It is designed to be easy to use and provides support for [Python 3.9](https://docs.python.org/3.9/) and above.

### Features:

- Easy-to-use API
- Compatible with Python 3.9 and above
- Extensive documentation

## Installation

To install the `steam-community-market` library, simply run:

- Linux / macOS:

```sh
python3 -m pip install -U steam-community-market
```

- Windows:

```sh
pip install -U steam-community-market
```

## Usage

To use the library, first import it in your Python script:

```python
from steam_community_market import *
```

Then, create an instance of the `Market` class, specifying the currency you want to use:

```python
market = Market(currency=Currency.USD)
```

Now you can use the various functions provided by the library to interact with the [Steam Community Market](https://steamcommunity.com/market/) API.

## Examples

Below you can find some examples on how to use different methods of the `steam-community-market` library.

First, let's import the required libraries for beautifully and correctly print our outputs, and define an item name constant:

```python
import json
import os

# Because we love "Mann Co. Supply Crate Key" <3
MANN_CO_SUPPLY_CRATE_KEY = "Mann Co. Supply Crate Key"
```

### Example: `get_overview`

```python
print(
    "get_overview:",
    json.dumps(
        market.get_overview(AppID.TF2, MANN_CO_SUPPLY_CRATE_KEY),
        indent=2,
        ensure_ascii=False,
    ),
    sep=os.linesep,
)
# get_overview:
# {
#   'success': True,
#   'lowest_price': '2,22€',
#   'volume': '18,015',
#   'median_price': '2,25€'
# }
```

### Example: `get_overviews`

```python
market_hash_names = [MANN_CO_SUPPLY_CRATE_KEY, "Name Tag", "The Festivizer"]
print(
    "get_overviews:",
    json.dumps(
        market.get_overviews(AppID.TF2, market_hash_names),
        indent=2,
        ensure_ascii=False,
    ),
    sep=os.linesep,
)
# get_overviews:
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
```

### Example: `get_lowest_price` / `get_price(lowest_price)`

```python
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
```

### Example: `get_prices`

```python
# get_prices
print(
    "get_prices:",
    json.dumps(
        market.get_prices(440, MANN_CO_SUPPLY_CRATE_KEY),
        indent=2,
        ensure_ascii=False
    ),
    sep=os.linesep,
)
# 440 - Team Fortress 2's App ID
# get_prices:
# {
#   'lowest_price': 2.22,
#   'median_price': 2.25
# }
```

### Example: `get_volume`

```python
# get_volume
# Getting information about "Steam" items is kind of weird, you need to look at its URL.
# IDF (CSGO Trading Card), you need to add 730- to. So it would be "730-IDF".
print(
    "get_volume:",
    market.get_volume(AppID.STEAM, "753-Sack of Gems"),
    sep=os.linesep,
)
# get_volume:
# 4982
```

For more examples and detailed explanations, please refer to the [official documentation](https://steam-community-market.readthedocs.io/) and the [examples module](https://github.com/offish/steam_community_market/blob/master/example.py).

## Support

If you have any questions, issues, or suggestions, please [create an issue](https://github.com/offish/steam-community-market/issues) on GitHub or join our [Discord server](https://discord.gg/t8nHSvA).

## Contributing

Contributions are always welcome! If you want to contribute, please [fork the repository](https://github.com/offish/steam-community-market/fork) and submit a pull request.

## Donations

If you find this library useful and would like to support the author and maintainer, you can donate using the following methods:

- Author - @offish

  [![Steam Trade](https://img.shields.io/static/v1?color=2a475e&label=Steam&logo=steam&message=Trade&style=flat)](https://steamcommunity.com/tradeoffer/new/?partner=293059984&token=0-l_idZR)

  - Bitcoin: `bc1qg275cltpez2dcedv2qucrtjxyhq4xurykstldk`

- Maintainer - @RoachxD

  [![Buy Me A Coffee](https://img.shields.io/static/v1?color=ffdd00&label=Coffee&logo=buy-me-a-coffee&message=Provide&style=flat)](https://www.buymeacoffee.com/roach)
  [![Ko-fi](https://img.shields.io/static/v1?color=ff5e5b&label=Ko-fi&logo=ko-fi&message=Provide&style=flat)](https://ko-fi.com/roachxd)

  - Bitcoin: `bc1qmyyratw3zaf6jj7azrvyr8vqmflpvhwzcf2zp7`
  - Ethereum: `0x8Ce07EA13A79bd40FeC8eEbC51BE5F2c69631031`

## License

`steam-community-market` is licensed under the [MIT License](https://github.com/offish/steam-community-market/blob/master/LICENSE).
