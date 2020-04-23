steam_community_market
======================
|pypi| |license| |stars| |issues| |repo_size| |chat|

|donate_steam| |donate|

Get prices and volumes of any item on the `Steam Community Market`_ using Python 3.

.. _Steam Community Market: https://steamcommunity.com/market/

.. contents:: Table of Contents
    :depth: 1


Installing
----------

Install and update using `pip`_:

.. code-block:: text

    pip install steam_community_market

.. _pip: https://pip.pypa.io/en/stable/quickstart/

Usage
-----

.. code-block:: python

    from steam_community_market import Market, AppID

    market = Market("USD")

    item = "AK-47 | Redline (Field Tested)"

    market.get_lowest_price(item, AppID.CSGO)
    14.98

    market.get_volume(item, 730)
    1097


`"USD"` can either be `ESteamCurrency`, `str`, `int` or empty. Find the currencies supported `here`_

.. _here: https://github.com/offish/steam_community_market/blob/master/steam_community_market/enums.py#L4


Documentation
-------------
Documentation will be added soon.

Links
-----
* `Documentation`_
* `Releases`_
* `Issue tracker`_
* `Discord`_
* `Donate`_


License
-------
MIT License

Copyright (c) 2020 `offish`_

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

.. _offish: https://offi.sh



.. _Documentation: https://offi.sh
.. _Releases: https://pypi.org/project/steam_community_market/
.. _Issue tracker: https://github.com/offish/steam_community_market/issues
.. _Discord: https://discord.gg/t8nHSvA
.. _Donate: https://www.paypal.me/0ffish

.. |pypi| image:: https://img.shields.io/pypi/v/steam_community_market.svg
    :target: https://pypi.org/project/steam_community_market
    :alt: Latest version released on PyPi

.. |license| image:: https://img.shields.io/github/license/offish/steam_community_market.svg
    :target: https://github.com/offish/steam_community_market/blob/master/LICENSE
    :alt: License

.. |stars| image:: https://img.shields.io/github/stars/offish/steam_community_market.svg
    :target: https://github.com/offish/steam_community_market/stargazers
    :alt: Stars

.. |issues| image:: https://img.shields.io/github/issues/offish/steam_community_market.svg
    :target: https://github.com/offish/steam_community_market/issues
    :alt: Issues

.. |repo_size| image:: https://img.shields.io/github/repo-size/offish/steam_community_market.svg
    :target: https://github.com/offish/steam_community_market
    :alt: Repo Size

.. |chat| image:: https://img.shields.io/discord/467040686982692865.svg
    :target: https://discord.gg/t8nHSvA
    :alt: Discord

.. |donate_steam| image:: https://img.shields.io/badge/donate-steam-green.svg
    :target: https://steamcommunity.com/tradeoffer/new/?partner=293059984&token=0-l_idZR
    :alt: Donate via Steam

.. |donate| image:: https://img.shields.io/badge/donate-paypal-blue.svg
    :target: https://www.paypal.me/0ffish
    :alt: Done via PayPal
