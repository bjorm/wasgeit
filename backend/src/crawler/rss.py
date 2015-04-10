import re
import locale
from datetime import datetime

from crawler.base import RssCrawler


class ISCCrawler(RssCrawler):
    def __init__(self):
        super().__init__()
        self.id = 1
        self.url = "http://www.isc-club.ch/programm?rss"
        self.file = "isc.xml"
        self.name = "ISC"

    def _extract_date(self, rss_entry):
        pattern = "[a-zA-Z]{2} ([0-9]{1,2}\. [a-zA-Z]+ [0-9]{4} \| [0-9]{2}[\.:][0-9]{2})"
        result = re.search(pattern, rss_entry.content[0].value)

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


class DachstockCrawler(RssCrawler):
    def __init__(self):
        super().__init__()
        self.id = 2
        self.url = "http://www.dachstock.ch/rss.xml"
        self.file = "dachstock.xml"
        self.name = "Dachstock"