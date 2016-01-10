from crawler.base import FacebookEventsCrawler

_venues = [
    {"name": "Playground Lounge", "url": "https://www.facebook.com/playgroundlounge/events?key=events"},
    {"name": "Brasserie Lorraine", "url": "https://www.facebook.com/pages/Genossenschaft-Restaurant-Brasserie-Lorraine/106714019391041?sk=events&ref=page_internal"},
    {"name": "Dean Wake", "url": "https://www.facebook.com/pages/Dean-Wake/113178252085227?sk=events&key=events"},
    {"name": "Kofmehl", "url": "https://www.facebook.com/tschieh/events?ref=page_internal"},
    {"name": "Coq d'Or", "url": "https://www.facebook.com/Coq.d.Or/events?ref=page_internal"},
    {"name": "KiFF", "url": "https://www.facebook.com/kiffaarau/events?ref=page_internal"},
    {"name": "Fri-Son", "url": "https://www.facebook.com/frisonclub/events?ref=page_internal"},
]

crawlers = [FacebookEventsCrawler(venue["name"], venue["url"]) for venue in _venues]
