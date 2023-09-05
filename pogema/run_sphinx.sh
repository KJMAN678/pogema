sphinx-quickstart docs -q -p pogema -a pogema -v 1.0 -l ja

# conf.py の変種

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# sys.path.insert(0, os.path.abspath("../"))

# extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
# include_patterns = ["*.rst"]

sphinx-apidoc -f -o ./docs ./docs/_build
