from datetime import datetime
import os

from facepy import GraphAPI

from crawler.base import VenueCrawler

_venues = [
    {"name": "Playground Lounge", "url": "playgroundlounge"},
    {"name": "Brasserie Lorraine", "url": "106714019391041"},
    {"name": "Dean Wake", "url": "113178252085227"},
    {"name": "Kofmehl", "url": "tschieh"},
    {"name": "Coq d'Or", "url": "Coq.d.Or"},
    {"name": "KiFF", "url": "kiffaarau"},
    {"name": "Fri-Son", "url": "frisonclub"},
]

graph = GraphAPI(os.environ['WASGEIT_ACCESS_TOKEN'])


class FacebookEventsCrawler(VenueCrawler):
    def __init__(self, name, url):
        super().__init__(name, url)

    def consume(self, data):
        for event in data['events']['data']:
            self.add_event({'date': self._parse_iso8601_date(event['start_time']),
                            'title': event['name'],
                            'link': "https://www.facebook.com/events/{}".format(event['id'])})

    def get_future(self, executor):
        return executor.submit(graph.get, self.url + '?fields=events')

    @staticmethod
    def _parse_iso8601_date(date_str):
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z').date()


crawlers = [FacebookEventsCrawler(venue["name"], venue["url"]) for venue in _venues]
