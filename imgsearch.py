import cloudinary
import requests
import json
import asyncio
from pyppeteer import launch

# patrick star meme twitter image URL
TEST_URL = "https://pbs.twimg.com/media/DXpdVIFVwAA0Bsx.jpg"

API_KEY = "AIzaSyBWaY98vwnvaBGvRxCCMH8YNOpUOcFtcaM"
CX = "004140975131308375580:oghwufu6das"
RESULT_COUNT = 10
QUERY = "'pbs.twimg.com/media/' inurl:twitter.com inurl:status"
BASE = "https://www.googleapis.com/customsearch/v1?q=%s&key=%s&cx=%s&image_url=%s)"

def imgsearch(url=TEST_URL):
    dump = []
    req_url = BASE % (QUERY, API_KEY, CX, url)
    resp = requests.get(req_url)
    # json comes back looking like this, looks and works just like a python 
    # {
    #   "items": [
    #      "link": "XXXXX",
    #   ]
    # }
    dump.append([ i["link"] for i in resp.json()["items"] ]) # so we parse the data like this
    return dump

# we'll just output this by running "py imgsearch.py"
if __name__ == "__main__":
    print(imgsearch())
