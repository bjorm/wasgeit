from concurrent import futures
from collections import defaultdict

from crawler.rss import crawlers as rss_crawlers
from crawler.html import crawlers as html_crawlers
from crawler.facebook import crawlers as fb_crawlers


class Agenda(object):
    def __init__(self):
        self._crawlers = rss_crawlers + html_crawlers + fb_crawlers
        self._do_crawl()

    def get_events(self, venue_ids):
        agenda = defaultdict(list)

        if len(venue_ids) == 0:
            venue_ids = {venue.id for venue in self._crawlers}

        for venue in [venue for venue in self._crawlers if venue.id in venue_ids]:
            for (event_date, events) in venue.get_events().items():
                agenda[event_date].extend(events)

        return agenda

    def get_venues(self):
        return [{'id': venue.id, 'name': venue.name} for venue in self._crawlers]

    def _do_crawl(self):
        with futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_crawler = {_crawler.get_future(executor): _crawler for _crawler in self._crawlers}
            for future in futures.as_completed(future_to_crawler):
                crawler = future_to_crawler[future]
                try:
                    data = future.result()
                    crawler.consume(data)
                except Exception as exc:
                    print('{} generated an exception: {}'.format(crawler, exc))