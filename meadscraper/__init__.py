# -*- coding: utf-8 -*-
"""Top-level package for meadscraper."""

__author__ = """nkanak"""
__email__ = 'nikos.kanakaris89@gmail.com'
__version__ = '0.1.0'

from bs4 import BeautifulSoup
import requests

from . import utils
from .announcement import Announcement
from .config import Config


def get_page_announcements(page_num,
                           as_objects=True,
                           download_descriptions=False):
    """ """
    page = requests.get(
        '%s/news/index//%s' % (Config.BASE_URL, page_num), timeout=10)
    soup = BeautifulSoup(page.content, Config.HTML_PARSER)
    elements = soup.find_all(id='new')
    announcements = []
    for el in elements:
        href = '%s%s' % (Config.BASE_URL, el.h3.a['href'].strip())
        id = href.split('/')[-1].strip()
        title = el.h3.a.text.strip()
        date, category = (lambda data: [data[0].strip(), data[1].strip()]
                          )(el.p.text.split(','))
        short_description = el.find_all('p', limit=2)[1].text.strip()
        description = utils.download_description(
            id) if download_descriptions is True else None
        mn = Announcement(id, href, title, date, category, short_description,
                          description)
        if as_objects is True:
            announcements.append(mn)
        else:
            announcements.append(mn.to_dict())
    return announcements


def get_announcement(id, as_object=True):
    """ """
    href = '%s/news/view/%s' % (Config.BASE_URL, id)
    page = requests.get(href, timeout=10)
    soup = BeautifulSoup(page.content, Config.HTML_PARSER)
    if soup.find(class_='no_results'):
        raise Exception('No results')
    title = soup.find(class_='content_text').h2.text.strip()
    date = soup.find(class_='content_text').p.text.strip()
    category = soup.find(id='breadcrumbs').find_all(
        'a', limit=3)[-1].text.strip()
    description = utils.compose_description(soup)
    announ = Announcement(
        id, href, title, date, category, description=description)
    return announ if as_object is True else announ.to_dict()
