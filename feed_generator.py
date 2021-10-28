from datetime import datetime
import random
import json

import arrow
import feedparser
from rfeed import Feed, Item

# returns the feed string given the JSON object

def generate_feed(link_data: list[dict], rss_link: str) -> str:
    data = []

    for link in link_data:
        feed = feedparser.parse(list(link.keys())[0])
        for i in range(list(link.values())[0]):
            newest = feed['entries'][i]
            data.append(Item(
                title=newest['title'],
                pubDate=arrow.get(newest['published'], 'DD MMM YYYY HH:mm:ss'),
                description=newest['summary'],
                link=newest['link']
            ))

    random.shuffle(data)

    return_feed = Feed(
        title='Aggregate RSS Feed',
        description='Aggregate RSS Feed',
        link=rss_link,
        lastBuildDate=datetime.now(),
        items=data,
    )

    return return_feed.rss()