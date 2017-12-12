#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yaty Lee'
SITENAME = u'Notes'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'cn'

THEME = 'pelican-themes/elegant'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['extract_toc']
MARKDOWN = {
	'extensions' : ['toc', 'fenced_code', 'codehilite(css_class=highlight)', 'tables'],
	'output_format': 'html5'
}

STATIC_PATHS = ['favicon.ico']
EXTRA_PATH_METADATA = {
	'favicon.ico': {'path': 'favicon.ico'}
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
