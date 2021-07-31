from datetime import datetime
import os
import random

import arrow
from dotenv import load_dotenv
import feedparser
from rfeed import Feed, Item

load_dotenv() # this is for development

links = []
with open('links.txt') as f:
    links = f.readlines()

data = []

for link in links:
    feed = feedparser.parse(link)
    newest = feed['entries'][0]
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
    link=os.getenv('RSS_LINK'),
    lastBuildDate=datetime.now(),
    items=data,
)

with open('feed.xml', 'w') as f:
    f.write(return_feed.rss())