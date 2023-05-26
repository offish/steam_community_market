************
Installation
************

To install the library, run the following command:

    * Linux / macOS:
        .. code-block:: sh

            python3 -m pip install -U steam-community-market
    
    * Windows:
        .. code-block:: sh

            pip install -U steam-community-market

Usage
-----

To use the library, first import it in your Python script:

.. code-block:: python

    from steam_community_market import *

Then, create a new instance of the :class:`Market <steam_community_market.market.instance>` class, specifying the currency you want to use:

.. code-block:: python

    market = Market(currency=Currency.USD)

Now you can use the various functions provided by the library to interact with the `Steam Community Market <https://steamcommunity.com/market>`__ API.