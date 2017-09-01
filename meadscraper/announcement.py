import datetime
import json

from . import utils
from .config import Config


class Announcement(object):
    """ """

    def __init__(self,
                 id,
                 url,
                 title,
                 date,
                 category,
                 short_description=None,
                 description=None):
        self.__id = int(id)
        self.__url = url
        self.__title = title
        self.__date = datetime.datetime.strptime(
            date, Config.DATE_FORMAT).date() if isinstance(date, str) else date
        self.__category = category
        self.__short_description = short_description
        self.__description = description

    def download_description(self):
        """ """
        self.__description = utils.download_description(self.__id)
        return self.__description

    def get_id(self):
        return self.__id

    def get_url(self):
        return self.__url

    def get_title(self):
        return self.__title

    def get_date(self):
        return self.__date

    def get_category(self):
        return self.__category

    def get_short_description(self):
        return self.__short_description

    def get_description(self, download_description=False):
        """ """
        if self.__description is None or download_description is True:
            self.download_description()
        return self.__description

    def to_dict(self):
        """ """
        return {
            'id': self.__id,
            'url': self.__url,
            'title': self.__title,
            'date': self.__date,
            'category': self.__category,
            'short_description': self.__short_description,
            'description': self.__description,
        }

    def to_json(self, as_object=True):
        """ """
        d = self.to_dict()
        d['date'] = d['date'].strftime(
            Config.DATE_FORMAT) if d['date'] is not None else d['date']
        dump = json.dumps(d)
        return json.loads(dump) if as_object is True else dump

    def __repr__(self):
        return '[%s][%s][%s]' % (self.__id, self.__url, self.__title)
