# -*- coding: utf-8 -*-
#
# 

import time

source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = u'Znuny'
copyright = u'2021-%s, Znuny Project' % time.strftime("%Y")
author = u'The Znuny Community and Team'


#version = u'1.0'
# The full version, including alpha/beta/rc tags.
#release = u'1.0'


language = 'en'

extensions = [
    'sphinx_copybutton',
    'sphinxcontrib.mermaid',
    'sphinx_tabs.tabs',
    'sphinx_fontawesome'
]

pygments_style = 'sphinx'
html_theme = 'sphinx_book_theme'
html_favicon = 'images/favicon.ico'

html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
    'css/code-tabs.css'
]
