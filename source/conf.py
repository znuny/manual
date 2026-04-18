# -*- coding: utf-8 -*-
#
# 

import os
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
    'sphinx_design',
    'sphinxext.opengraph',
]

# SEO role, set by CI per branch build: 'stable' | 'lts' | 'archived'.
DOCS_ROLE   = os.environ.get('ZNUNY_DOCS_ROLE', 'archived')
DOCS_BRANCH = os.environ.get('ZNUNY_DOCS_BRANCH', 'znuny-7_3')

_ALIAS = {'stable': 'znuny', 'lts': 'znuny_lts'}

if DOCS_ROLE in _ALIAS:
    html_baseurl = f'https://doc.znuny.org/{_ALIAS[DOCS_ROLE]}/'
    extensions.append('sphinx_sitemap')
    sitemap_url_scheme = '{link}'
else:
    html_baseurl = f'https://doc.znuny.org/{DOCS_BRANCH}/'
    html_meta = {'robots': 'noindex, follow'}

ogp_site_url  = html_baseurl
ogp_site_name = 'Znuny Documentation'

pygments_style = 'sphinx'
html_theme = 'sphinx_book_theme'
html_favicon = 'images/favicon.ico'

html_theme_options = {
    "switcher": {
        "json_url": "https://doc.znuny.org/version.json",
        "version_match": DOCS_BRANCH,
    },
    "primary_sidebar_end": ["version-switcher"],
    "repository_url": "https://github.com/znuny/manual",
    "repository_branch": DOCS_BRANCH,
    "use_repository_button": True,
    "use_issues_button": False,
    "use_edit_page_button": False,
}

html_static_path = ['_static']
html_css_files = [
    'css/custom.css'
]

linkcheck_allowed_redirects = {
    # All HTTP redirections from the source URI to the canonical URI will be treated as "working".
    #r'https?://.*': r'https?://.*',
    r'https://(www\.)?znuny\.(com|org).*': r'https://www\.znuny\.(com|org).*',
    r'https://github\.com.*': r'https://github\.com.*',
    r'https://github.com/znuny/.*': r'https://raw.githubusercontent.com/znuny/.*',
    r'https://.+.microsoft.com/.*': r'https://.+.microsoft.com/.*',
    r'http://.+': r'https://.+',
    r'https://discord.gg/.+': r'https://discord.com/.+'
}

linkcheck_ignore = [
    r'https://download.znuny.org/releases/znuny-\d.\d.\d+.tar.gz',
    r'https://github.com/znuny/Znuny/commits/rel-.+',
    r'https://github.com/znuny/Znuny/blob/.+#L\d+',
    r'https://.+\.wikipedia\.org/.+',
    r'.+/cgi-bin/.+'
]
