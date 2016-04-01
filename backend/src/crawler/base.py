import urllib
from collections import defaultdict
from datetime import date
import logging

import feedparser
from lxml import html
from pyquery import PyQuery as Pq

# TODO introduce class for events


class VenueCrawler(object):
    _event_id = 0
    _venue_id = 0

    def __init__(self, name, url):
        # TODO push venue details into dict
        self.id = VenueCrawler._get_next_venue_id()
        self.file = None
        self.name = name
        self.url = url
        self.entries = defaultdict(list)
        self.log = logging.getLogger(name)

    def get_events(self):
        return self.entries

    def get_future(self, executor):
        pass

    def consume(self, data):
        pass

    def add_event(self, event):
        if event['date'] >= date.today():
            date_str = event['date'].isoformat()
            event['venue'] = self.name
            event['id'] = self._get_next_event_id()
            self.log.debug("Added event to agenda: '{}'".format(event))
            self.entries[date_str].append(event)
        else:
            self.log.debug("Discarded event because it happens in the past: '{}'".format(event))

    @staticmethod
    def _get_next_event_id():
        """Events are not created by multiple threads hence no lock."""
        VenueCrawler._event_id += 1
        return VenueCrawler._event_id

    @staticmethod
    def _get_next_venue_id():
        """Venues are not created by multiple threads hence no lock."""
        VenueCrawler._venue_id += 1
        return VenueCrawler._venue_id


class HtmlCrawler(VenueCrawler):
    def __init__(self, name, url):
        super().__init__(name, url)
        self.timeout = 60

    def load_url(self, url):
        return urllib.request.urlopen(url, timeout=self.timeout).read()

    def get_future(self, executor):
        req = urllib.request.Request(self.url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        return executor.submit(self.load_url, req)

    def consume(self, data):
        # TODO naming
        d = Pq(html.fromstring(data))
        self._analyze_dom(d)

    def _analyze_dom(self, d):
        pass




class RssCrawler(VenueCrawler):
    def __init__(self, name, url):
        super().__init__(name, url)

    def consume(self, data):
        for entry in data.entries:
            event_date = self._extract_date(entry)
            if event_date is not None:
                event = self._create_event(entry, event_date)
                self.add_event(event)

    @staticmethod
    def _create_event(rss_entry, d):
        return {'date': d, 'title': rss_entry.title, 'link': rss_entry.link}

    def _extract_date(self, rss_entry):
        time_struct = rss_entry['published_parsed']
        return date(time_struct.tm_year, time_struct.tm_mon, time_struct.tm_mday)

    def get_future(self, executor):
        return executor.submit(feedparser.parse, self.url)

