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

# Social widget, use the fontawesome icon label to have it show on your website
SOCIAL = (
    ("fa-brands fa-github", "https://github.com/mr4tt"),
    ("fa-regular fa-envelope", "mailto:hello.mrat@gmail.com")
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
THEME = 'themes/Peli-Kiera'
ARTICLE_PATHS = ['comics', 'case_studies', "misc"]
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

#PLUGIN_PATHS = ['pelican-plugins']
# can add readtime if desired
PLUGINS = ['neighbors']

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico', 'extra/og-default.png', 'extra/resume_it.pdf']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 
                       'extra/favicon.ico': {'path': 'favicon.ico'}, 
                       'extra/resume_it.pdf': {'path': 'resume.pdf'}, }

# IGNORE_FILES = ['.test*']

# MENUITEMS = [
#     ('Google', 'http://www.google.com')
# ]