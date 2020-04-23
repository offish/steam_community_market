# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import re
import sys

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('extensions'))


# -- Project information -----------------------------------------------------

project = 'steam community market'
copyright = '2020, offish'
author = 'offish'

with open('../steam_community_market/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

# The full version, including alpha/beta/rc tags
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'builder',
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'details',
    'exception_hierarchy'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


autodoc_member_order = 'bysource'


html_theme_options = {
    'description': 'by offish',
    'github_user': 'offish',
    'github_repo': 'steam_community_market',
    'github_button': 'true',
    'github_banner': 'true',
    'fixed_sidebar': 'true',
    'donate_url': 'https://steamcommunity.com/tradeoffer/new/?partner=293059984&token=0-l_idZR',
}

# Skal endres senere.
"""
{ 
    # Under skal flyttes til _static/custom.css
    
    'caption_font_size': '20px',
    'base_bg': '#282A36',  # bakgrunn
    'code_font_family': "'Consolas', 'Menlo', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', monospace'",
    'link': '#5EBFE4',  # alle link farger
    'sidebar_link': '#D764A7',
    'body_bg': '#191A21',
    'highlight_bg': '#383A59',
    'viewcode_target_bg': '#ffd700',
    'code_text': '#B380CF',  # etter class og funksjon navn
    'body_text': '#F8F7F0',  # vanlig tekst og overskrifter
    'footer_text': '#BD93F9',  # footer text farge (bra)
    'gray_2': '#282A36',  # code embeds bra
    'link_hover': '#3CD872', # link hover farge bra
    'narrow_sidebar_bg': '#191A21', # når sidebar er mobilview (bra)
    'narrow_sidebar_link': '#D764A7',  # link farger i mobilview
    'pre_bg': '#343746',  # code blocks bla
    'sidebar_header': '#47CF5A',  # navigation, quick search og donate support
    'sidebar_search_button': '#F7F7F1', # søk button
    'sidebar_text': '#F6F3ED',  # by offish og contents
}
"""