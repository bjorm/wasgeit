from datetime import datetime

from pyquery import PyQuery as Pq

from crawler.base import HtmlCrawler


class KairoCrawler(HtmlCrawler):
    def __init__(self):
        super().__init__()
        self.id = 3
        self.url = "http://www.cafe-kairo.ch/kultur"
        self.name = "Cafe Kairo"

    def _analyze_dom(self, d):
        for article in d("article"):
            event_date = self._parse_date(Pq(article).find(".concerts_date time").text()[3:])
            title = Pq(article).find("h1").text()
            url = self._build_url(Pq(article).attr['id'])
            if event_date is not None:
                self.add_event({'title': title, 'date': event_date, 'link': url})

    @staticmethod
    def _parse_date(date_str):
        try:
            return datetime.strptime(date_str, '%d.%m.%Y').date()
        except ValueError as exc:
            print(exc)
            return None

    def _build_url(self, node_id):
        return "{}#{}".format(self.url, node_id)


crawlers = [KairoCrawler()]