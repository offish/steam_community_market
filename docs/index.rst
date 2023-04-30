.. steam-community-market documentation master file, created by
   sphinx-quickstart on Sat Apr 11 21:02:34 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

**********************
steam-community-market
**********************

`steam-community-market <https://github.com/offish/steam_community_market/>`__ is a `Python <https://www.python.org/>`__ library that provides a simple and efficient way to interact with the `Steam Community Market`_ API. It is designed to be easy to use and provides support for `Python 3.9 <https://docs.python.org/3.9/>`__ and above.

.. image:: https://img.shields.io/pypi/pyversions/steam-community-market?color=0067a3&label=Supported%20Versions&logo=pypi&logoColor=0067a3
    :target: https://pypi.org/project/steam-community-market/
.. image:: https://img.shields.io/pypi/dm/steam-community-market?color=0067a3&label=Downloads&logo=pypi&logoColor=0067a3
    :target: https://pypi.org/project/steam-community-market/
.. image:: https://img.shields.io/pypi/l/steam-community-market?color=0067a3&label=License&logo=pypi&logoColor=0067a3
    :target: https://pypi.org/project/steam-community-market/
.. image:: https://img.shields.io/github/issues-raw/offish/steam_community_market?color=ffffff&label=Open%20Issues&logo=github
    :target: https://github.com/offish/steam_community_market/issues
.. image:: https://img.shields.io/github/stars/offish/steam_community_market?color=ffffff&label=Stargazers&logo=github
    :target: https://github.com/offish/steam_community_market/stargazers
.. image:: https://img.shields.io/discord/467040686982692865?color=7289da&label=Discord&logo=discord&logoColor=7289da
    :target: https://discord.gg/t8nHSvA

Using this library
------------------

:doc:`Installation <pages/guidelines/installation>`
    How to install the library and integrate it into your project.

:doc:`License <pages/guidelines/license>`
    The license that this library is released under.

Class Documentation
-------------------

:doc:`Market <pages/classes/market>`
    The main class for interacting with the `Steam Community Market`_ API.

:doc:`Currencies <pages/classes/currencies>`
    A namespace containing all of the currencies used by the library.

:doc:`Enums <pages/classes/enums>`
    A class containing all of the enums used by the library.

:doc:`Exceptions <pages/classes/exceptions>`
    A class containing all of the exceptions used by the library.

.. Common Links

.. _Steam Community Market: https://steamcommunity.com/market/

.. Hidden TOCs

.. toctree::
    :caption: Library Guidelines
    :maxdepth: 2
    :hidden:

    pages/guidelines/installation
    pages/guidelines/license

.. toctree::
    :caption: Classes Documentation
    :maxdepth: 2
    :hidden:

    pages/classes/market
    pages/classes/currencies
    pages/classes/decorators
    pages/classes/enums
    pages/classes/exceptions
    pages/classes/requests