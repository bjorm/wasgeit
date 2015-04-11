from concurrent import futures
from collections import defaultdict

from crawler.rss import *
from crawler.html import *
from crawler.facebook import *


class Agenda(object):
    def __init__(self):
        self._venues = [ISCCrawler(), DachstockCrawler(), KairoCrawler(), PlaygroundLoungeCrawler(), BrasserieLorraineCrawler(), DeanWakeCrawler()]
        self._crawl_venues()

    def get_events(self, venue_ids):
        agenda = defaultdict(list)

        if len(venue_ids) == 0:
            venue_ids = {venue.id for venue in self._venues}

        for venue in [venue for venue in self._venues if venue.id in venue_ids]:
            for (event_date, events) in venue.get_events().items():
                agenda[event_date].extend(events)

        return agenda

    def get_venues(self):
        return [{'id': venue.id, 'name': venue.name} for venue in self._venues]

    def _crawl_venues(self):
        with futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_venue = {_venue.get_future(executor): _venue for _venue in self._venues}
            for future in futures.as_completed(future_to_venue):
                venue = future_to_venue[future]
                try:
                    data = future.result()
                    venue.consume(data)
                except Exception as exc:
                    print('{} generated an exception: {}'.format(venue, exc))