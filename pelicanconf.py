AUTHOR = 'mrat'
SITENAME = 'starly dot dev'
# SITEURL = "http://localhost:8000"
# SITEURL = "https://mr4tt.github.io/csmic"
SITEURL = "https://starly.dev"
# SITESUBTITLE = 'Waiting for something to happen?'

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("github", "https://github.com/mr4tt"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = 'themes/Peli-Kiera'
ARTICLE_PATHS = ['comics', 'case_studies', "misc"]
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

#PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors']

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico', 'extra/og-default.png']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/favicon.ico': {'path': 'favicon.ico'},}

# MENUITEMS = [
#     ('Google', 'http://www.google.com')
# ]