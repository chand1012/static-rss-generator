from datetime import datetime
import os
import random
import json

import arrow
from dotenv import load_dotenv
import feedparser
from rfeed import Feed, Item

load_dotenv() # this is for development

links = []

with open('links.json') as f:
    links = json.loads(f.read())

# print(links)

data = []

for link in links:
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
    link=os.getenv('RSS_LINK'),
    lastBuildDate=datetime.now(),
    items=data,
)

with open('feed.xml', 'w') as f:
    f.write(return_feed.rss())