""" conf.py
    Configuration file for the Sphinx documentation builder.

   isort:skip_file
"""

# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# import sys
# sys.path.insert(0, os.path.abspath('.'))
import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import pathlib
import re

import packaging


def get_version_from_file(path):
    with open(path) as fp:
        match = re.search(r'__version__\s*=\s*[\'"]([^\'"]+)[\'"]', fp.read())
        if match:
            version = match.group(1)
        else:
            raise ValueError(f"version string not found ({path})")
    return packaging.version.Version(version)


src_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "bmi_geotiff")
)
# sys.path.insert(0, src_dir)
docs_dir = pathlib.Path(__file__).parent
version_file = os.path.join(src_dir, "_version.py")

# The master toctree document.
master_doc = "index"

# -- Project information -----------------------------------------------------

project = "bmi-geotiff"
author = "Community Surface Dynamics Modeling System"
this_year = datetime.date.today().year
copyright = f"{this_year}, {author}"

v = get_version_from_file(version_file)
version = f"{v.major}.{v.minor}"
release = v.public

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/powered-by-logo-header.png"

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    "index": [
        "sidebarintro.html",
        "links.html",
        "sourcelink.html",
        "searchbox.html",
    ],
    "**": [
        "sidebarintro.html",
        "links.html",
        "sourcelink.html",
        "searchbox.html",
    ],
}
