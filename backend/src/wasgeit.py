import feedparser
from concurrent import futures
from datetime import date, datetime
from collections import defaultdict
import locale
import re


class Venue(object):
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


class VenueWithRssFeed(Venue):
    def __init__(self):
        super().__init__()

    def consume(self, data):
        for entry in data.entries:
            event_date = self._extract_date(entry)
            if event_date is not None:
                event = self._create_event(entry, event_date)
                self.entries[event_date.isoformat()].append(event)

    def _create_event(self, rss_entry, d):
        return {'date': d.isoformat(), 'title': rss_entry.title, 'link': rss_entry.link, 'venue': self.name}

    def _extract_date(self, rss_entry):
        time_struct = rss_entry['published_parsed']
        return date(time_struct.tm_year, time_struct.tm_mon, time_struct.tm_mday)

    def get_future(self, executor):
        return executor.submit(feedparser.parse, self.file)


class ISC(VenueWithRssFeed):
    def __init__(self):
        super().__init__()
        self.id = 1
        self.url = "http://www.isc-club.ch/programm?rss"
        self.file = "isc.xml"
        self.name = "ISC"

    def _extract_date(self, rss_entry):
        result = re.search("[a-zA-Z]{2} ([0-9]{1,2}\. [a-zA-Z]+ [0-9]{4} \| [0-9]{2}[\.:][0-9]{2})", rss_entry.content[0].value)

        if result is None:
            print("No date found in '{}'".format(rss_entry.content[0].value))
            return None
        else:
            pat = re.compile("(\d{2})\.(\d{2})")
            match = pat.sub("\g<1>:\g<2>", result.group(1))
            try:
                locale.setlocale(locale.LC_TIME, 'de_CH')
                return datetime.strptime(match, '%d. %B %Y | %H:%M').date()
            except ValueError:
                print("Unparseable date: {}".format(match))
                return None


class Dachstock(VenueWithRssFeed):
    def __init__(self):
        super().__init__()
        self.id = 2
        self.url = "http://www.dachstock.ch/rss.xml"
        self.file = "dachstock.xml"
        self.name = "Dachstock"


class Agenda(object):
    def __init__(self):
        self._venues = [ISC(), Dachstock()]
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
                except Exception as exc:
                    print('%r generated an exception: %s' % (venue, exc))
                else:
                    venue.consume(data)
                    for (event_date, events) in venue.get_events().items():
                        agenda[event_date].extend(events)

        return agenda
