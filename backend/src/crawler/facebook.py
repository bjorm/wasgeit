from crawler.base import FacebookEventsCrawler


class PlaygroundLoungeCrawler(FacebookEventsCrawler):
    def __init__(self):
        super().__init__()
        self.url = "https://www.facebook.com/playgroundlounge/events?key=events"
        self.id = 4
        self.name = "Playground Lounge"


class BrasserieLorraineCrawler(FacebookEventsCrawler):
    def __init__(self):
        super().__init__()
        self.url = "https://www.facebook.com/pages/Genossenschaft-Restaurant-Brasserie-Lorraine/106714019391041?sk=events&ref=page_internal"
        self.id = 5
        self.name = "Brasserie Lorraine"


class DeanWakeCrawler(FacebookEventsCrawler):
    def __init__(self):
        super().__init__()
        self.url = "https://www.facebook.com/pages/Dean-Wake/113178252085227?sk=events&key=events"
        self.id = 6
        self.name = "Dean Wake"


class TurnhalleCrawler(FacebookEventsCrawler):
    def __init__(self):
        super().__init__()
        self.url = "https://www.facebook.com/turnhalle.ch/events?ref=page_internal"
        self.id = 7
        self.name = "Turnhalle"


crawlers = [PlaygroundLoungeCrawler(), BrasserieLorraineCrawler(), DeanWakeCrawler(), TurnhalleCrawler()]