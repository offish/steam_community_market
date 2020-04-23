.. currentmodule:: steam_community_market

market.py
=========


Market
------
.. autoclass:: Market
    :members:

UNSUPPORTED_CURRENCY
--------------------
.. code:: python

    "RUB",
    "VND",
    "KRW",
    "CLP",
    "PEN",
    "COP",
    "CRC"

These currencies are are supported, but won't 
be converted to :class:`float` due to "weird" formatting.

.. code:: python

    from steam_community_market import Market

    market = Market("RUB")

    market.get_lowest_price("Mann Co. Supply Crate Key", 440)

.. code:: text

    163,80 pуб.

.. versionadded:: 1.2.0
