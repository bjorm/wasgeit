from concurrent import futures
from collections import defaultdict

from crawler.rss import *
from crawler.html import *


class Agenda(object):
    def __init__(self):
        self._venues = [ISCCrawler(), DachstockCrawler(), KairoCrawler()]
        self.agenda = self._load_events_from_venues()

    def get(self):
        return self.agenda

    def _load_events_from_venues(self):
        agenda = defaultdict(list)

        with futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_venue = {_venue.get_future(executor): _venue for _venue in self._venues}
            for future in futures.as_completed(future_to_venue):
                venue = future_to_venue[future]
                try:
                    data = future.result()
                    venue.consume(data)
                except Exception as exc:
                    print('{} generated an exception: {}'.format(venue, exc))
                else:
                    for (event_date, events) in venue.get_events().items():
                        agenda[event_date].extend(events)

        return agenda
