import urllib.request
from datetime import datetime
import re
from collections import defaultdict
from datetime import date
import locale

import feedparser
from lxml import html
from pyquery import PyQuery as Pq


class VenueCrawler(object):
    def __init__(self):
        # TODO push venue details into dict
        self.id = None
        self.file = None
        self.name = None
        self.url = None
        self.entries = defaultdict(list)

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
            self.entries[date_str].append(event)


class HtmlCrawler(VenueCrawler):
    def __init__(self):
        super().__init__()
        self.timeout = 60

    def load_url(self, url):
        return urllib.request.urlopen(url, timeout=self.timeout).read()

    def get_future(self, executor):
        return executor.submit(self.load_url, self.url)

    def consume(self, data):
        # TODO naming
        d = Pq(html.fromstring(data))
        self._analyze_dom(d)

    def _analyze_dom(self, d):
        pass


class FacebookEventsCrawler(HtmlCrawler):
    def __init__(self):
        super().__init__()

    def consume(self, data):
        # TODO clean up
        hidden_markup = re.compile("<!-- (.*TimelineSection.*) -->")
        match = re.search(hidden_markup, data.decode('utf-8'))
        event_timeline = Pq(match.group(1))
        self._analyze_dom(event_timeline)

    def _analyze_dom(self, event_timeline):
        # TODO clean up
        event_items = [Pq(event) for event in event_timeline.find('table').filter(self.is_timeline_event)]
        for event in event_items:
            event_element = event.find('div > a[data-hovercard]')
            title = event_element.text()
            event_url_path_segment = event_element.attr['href']
            day_month_str = event.find('td:first > div').text()
            event_date = self._create_date(day_month_str)
            link = self._create_link(event_url_path_segment)
            self.add_event({'title': title, 'date': event_date.date(), 'link': link})

    @staticmethod
    def is_timeline_event(id, element):
        return element.attrib.get('id', '').startswith('timeline_event_item')

    @staticmethod
    def _create_link(path):
        return "{}{}".format("http://facebook.com", path)

    @staticmethod
    def _create_date(day_month_str):
        locale.setlocale(locale.LC_TIME, 'de_CH')
        return datetime.strptime('{} {}'.format(day_month_str, date.today().year), '%b %d %Y')


class RssCrawler(VenueCrawler):
    def __init__(self):
        super().__init__()

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

