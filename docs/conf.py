# -- Project information -----------------------------------------------------

project = "Sphinx Book Theme"
copyright = "2020, Executable Book Project"
author = "Executable Book Project"

master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["myst_parser", "myst_nb", "sphinx_copybutton", "sphinx_togglebutton"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "_static/logo.png"
html_title = "Sphinx Book Theme"
html_copy_source = True
html_sourcelink_suffix = ""
html_favicon = "_static/logo.png"
# html_theme_options = {"github_url": "https://github.com/ExecutableBookProject/myst-nb"}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
jupyter_sphinx_require_url = ""

html_theme_options = {
    "binder_config": {
        "use_binder_button": True,
        "binderhub_url": "https://mybinder.org",
        "path_to_docs": "docs",
        "repository_url": "https://github.com/ExecutableBookProject/sphinx-book-theme",
    }
}
