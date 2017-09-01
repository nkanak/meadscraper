import requests
from bs4 import BeautifulSoup

from .config import Config


def compose_description(soup):
    return '\n'.join([
        p.text.strip() for p in soup.find(class_='content_text').find_all('p')
    ][1:]).strip()


def download_description(id):
    page = requests.get('%s/news/view/%s' % (Config.BASE_URL, id), timeout=10)
    soup = BeautifulSoup(page.content, Config.HTML_PARSER)
    return compose_description(soup)
