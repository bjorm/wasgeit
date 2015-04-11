import re
from datetime import datetime, date

from pyquery import PyQuery as Pq

from crawler.base import HtmlCrawler


class FacebookEventsCrawler(HtmlCrawler):
    def __init__(self):
        self.fb_page_url = None
        self.event_page_postfix = "events?key=events"
        super().__init__()

    def consume(self, data):
        hidden_markup = re.compile("<!-- (.*TimelineSection.*) -->")
        match = re.search(hidden_markup, data.decode('utf-8'))
        event_timeline = Pq(match.group(1))
        event_items = [Pq(event) for event in event_timeline.find('table').filter(FacebookEventsCrawler.is_timeline_event)]
        for event in event_items:
            title = event.find('div > a[data-hovercard]').text()
            link = event.find('div > a[data-hovercard]').attr['href']
            day_month_str = event.find('td:first > div').text()
            event_date = datetime.strptime('{} {}'.format(day_month_str, date.today().year), '%b %d %Y')
            self.add_event({'title': title, 'date': event_date.date(), 'link': "{}{}".format("http://facebook.com", link), 'venue': self.name})


    @staticmethod
    def is_timeline_event(id, element):
        return element.attrib.get('id', '').startswith('timeline_event_item')


class PlaygroundLoungeCrawler(FacebookEventsCrawler):
    def __init__(self):
        super().__init__()
        self.fb_page_url = "https://www.facebook.com/playgroundlounge"
        self.url = "{}/{}".format(self.fb_page_url, self.event_page_postfix)
        self.id = 4
        self.name = "Playground Lounge"


