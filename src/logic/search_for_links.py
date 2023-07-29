"""

"""
# ------------------------------------------------------- #
#                     imports
# ------------------------------------------------------- #
import re
from bs4 import BeautifulSoup
import urllib.request
from zk_tools.logging_handle import logger

# ------------------------------------------------------- #
#                   definitions
# ------------------------------------------------------- #
MODULE_LOGGER_HEAD = "search_for_links ->"

# ------------------------------------------------------- #
#                   global variables
# ------------------------------------------------------- #
VOE_PATTERN = re.compile(r"'mp4': '(?P<url>.+)'")

# ------------------------------------------------------- #
#                      functions
# ------------------------------------------------------- #


def redirect(site_url, link, button):
    html_page = urllib.request.urlopen(link)
    soup = BeautifulSoup(html_page, features="html.parser")
    for link in soup.findAll("a", {"class": "watchEpisode"}):
        provider_name = link.find("h4").text
        if provider_name == button:
            redirecting_link = site_url + link.get("href")
            return redirecting_link, provider_name


def find_cache_url(url, provider):
    logger.debug(MODULE_LOGGER_HEAD + "Enterd {} to cache".format(provider))
    html_page = urllib.request.urlopen(url)
    if provider == "Vidoza":
        soup = BeautifulSoup(html_page, features="html.parser")
        cache_link = soup.find("source").get("src")
    elif provider == "VOE":
        cache_link = VOE_PATTERN.search(html_page.read().decode('utf-8')).group("url")
    logger.debug(MODULE_LOGGER_HEAD + "Exiting {} to Cache".format(provider))
    return cache_link

# ------------------------------------------------------- #
#                      classes
# ------------------------------------------------------- #


# ------------------------------------------------------- #
#                       main
# ------------------------------------------------------- #

