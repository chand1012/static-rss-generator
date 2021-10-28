import os
import json

from dotenv import load_dotenv

from feed_generator import generate_feed

load_dotenv() # this is for development

links = []

with open('links.json') as f:
    links = json.loads(f.read())

return_feed = generate_feed(links, os.getenv('RSS_LINK'))

with open('feed.xml', 'w') as f:
    f.write(return_feed)