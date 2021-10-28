import os

from feed_generator import generate_feed

from fastapi import FastAPI
from fastapi.responses import Response
import ujson as json
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

LINK_JSON_FILE = os.environ.get('LINK_JSON_FILE', 'links.json')

@app.get("/feed.xml")
async def rss():
    links = []

    with open(LINK_JSON_FILE) as f:
        links = json.loads(f.read())

    return_feed = generate_feed(links, os.getenv('RSS_LINK'))

    return Response(return_feed, media_type='application/xml')