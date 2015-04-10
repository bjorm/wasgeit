import urllib.request
import feedparser
from collections import defaultdict
from datetime import date
from lxml import html
from pyquery import PyQuery as Pq


class VenueCrawler(object):
    def __init__(self):
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
        d = Pq(html.fromstring(data))
        self._analyze_dom(d)

    def _analyze_dom(self, d):
        pass


class RssCrawler(VenueCrawler):
    def __init__(self):
        super().__init__()

    def consume(self, data):
        for entry in data.entries:
            event_date = self._extract_date(entry)
            if event_date is not None:
                event = self._create_event(entry, event_date)
                self.add_event(event)

    def _create_event(self, rss_entry, d):
        return {'date': d, 'title': rss_entry.title, 'link': rss_entry.link, 'venue': self.name}

    def _extract_date(self, rss_entry):
        time_struct = rss_entry['published_parsed']
        return date(time_struct.tm_year, time_struct.tm_mon, time_struct.tm_mday)

    def get_future(self, executor):
        return executor.submit(feedparser.parse, self.file)
