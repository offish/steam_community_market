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

sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("extensions"))


# -- Project information -----------------------------------------------------

project = "steam-community-market"
slug = re.sub(r"\W+", "-", project.lower())
author = "offish"
copyright = f"2020 - 2023 {author}"
language = "en"

with open("../steam_community_market/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    )[1]

# The full version, including alpha/beta/rc tags
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "builder",
    "details",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "exception_hierarchy",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
]

intersphinx_mapping = {"py": ("https://docs.python.org/3.9", None)}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

root_doc = "index"

# -- Options for HTML output -------------------------------------------------

html_favicon = "_static/favicon.ico"

html_logo = "_static/logo.png"

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 2,
    "includehidden": True,
    "logo_only": True,
    "prev_next_buttons_location": None,
    "style_nav_header_background": "#2a475e",
}

napoleon_google_docstring = False
napoleon_use_ivar = True

autodoc_member_order = "bysource"
