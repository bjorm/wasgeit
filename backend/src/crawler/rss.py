import re
import locale
from datetime import datetime

from crawler.base import RssCrawler


class ISCCrawler(RssCrawler):
    def __init__(self):
        super().__init__("ISC", "http://www.isc-club.ch/programm?rss")

    def _extract_date(self, rss_entry):
        pattern = "[a-zA-Z]{2} ([0-9]{1,2}\. [a-zA-Z]+ [0-9]{4} \| [0-9]{2}[\.:][0-9]{2})"
        result = re.search(pattern, rss_entry.content[0].value)

        if result is None:
            self.log.warn("No date found in '{}'".format(rss_entry.content[0].value))
            return None
        else:
            pat = re.compile("(\d{2})\.(\d{2})")
            match = pat.sub("\g<1>:\g<2>", result.group(1))
            locale.setlocale(locale.LC_TIME, 'de_CH.UTF-8')
            for month_pattern in ['%b', '%B']:
                try:
                    date_format = '%d. {} %Y | %H:%M'.format(month_pattern)
                    return datetime.strptime(match, date_format).date()
                except ValueError:
                    self.log.warning("Could not parse '{}' with '{}'".format(match, date_format))

            self.log.warn("Aborting parsing of date '{}'".format(match))
            return None


crawlers = [ISCCrawler()]