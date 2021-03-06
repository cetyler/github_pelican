#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Christopher Tyler'
SITENAME = 'Christopher Tyler R&D Test Engineer'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'pelican-themes/pelican-bootstrap3'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['pelican-plugins']

from pelican_jupyter import markup as nb_markup
PLUGINS = ['i18n_subsites',
           'sitemap',
           nb_markup,
          ]


BIND = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Automate the Boring Stuff', 'https://automatetheboringstuff.com/'),
         ('Practical Business Python', 'https://pbpython.com'),
         ('Real Python', 'https://realpython.com'),
         ('Talk Python to Me', 'https://talkpython.fm/'),
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/christopheretyler'),
          ('GitHub', 'https://github.com/cetyler'),)

DEFAULT_PAGINATION = 10

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'always',
        'indexes': 'hourly',
        'pages': 'monthly'
    }
}

# Jupyter Notebook
MARKUP = ('md', 'ipynb')

IGNORE_FILES = ['.ipynb_checkpoints'] 
IPYNB_MARKUP_USE_FIRST_CELL = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True