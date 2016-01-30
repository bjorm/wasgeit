from datetime import datetime
import locale

from pyquery import PyQuery as Pq

from crawler.base import HtmlCrawler


class KairoCrawler(HtmlCrawler):
    def __init__(self):
        super().__init__("Cafe Kairo", "http://www.cafe-kairo.ch/kultur")

    def _analyze_dom(self, d):
        for article in d("article"):
            event_date = self._parse_date(Pq(article).find(".concerts_date time").text()[3:])
            title = Pq(article).find("h1").text()
            url = self._build_url(Pq(article).attr['id'])
            if event_date is not None:
                self.add_event({'title': title, 'date': event_date, 'link': url})

    def _parse_date(self, date_str):
        try:
            return datetime.strptime(date_str, '%d.%m.%Y').date()
        except ValueError as exc:
            self.log.error(exc)
            return None

    def _build_url(self, node_id):
        return "{}#{}".format(self.url, node_id)


class TurnhalleCrawler(HtmlCrawler):
    def __init__(self):
        super().__init__("Turnhalle", "http://www.turnhalle.ch")

    def _analyze_dom(self, d):
        locale.setlocale(locale.LC_TIME, 'de_CH')

        for event in d(".event-inner-header"):
            title = "{}: {}".format(Pq(event).find("h1").text(), Pq(event).find("h2").text())
            dom_id = d(event).parent().parent().attr('id')
            link = "{}#{}".format(self.url, dom_id)
            event_date = self._parse_date(Pq(event).find("h3").text())
            if event_date is not None:
                self.add_event({"title": title, "date": event_date, "link": link})

    def _parse_date(self, full_date_string):
        event_date_str = full_date_string.split("|")[1].strip()
        try:
            return datetime.strptime(event_date_str, '%d. %B %Y').date()
        except ValueError as exc:
            self.log.error(exc)
            return None


crawlers = [KairoCrawler(), TurnhalleCrawler()]
