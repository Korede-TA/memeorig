# import cloudinary
import requests
import urllib
# import asyncio
# from pyppeteer import launch

# patrick star meme twitter image URL
TEST_URL = "https://pbs.twimg.com/media/DXpdVIFVwAA0Bsx.jpg"

API_KEY = "AIzaSyBWaY98vwnvaBGvRxCCMH8YNOpUOcFtcaM"
CX = "004140975131308375580:oghwufu6das"
RESULT_COUNT = 10
QUERY = "%s 'pbs.twimg.com/media/' inurl:twitter.com inurl:status"
BASE = "https://www.googleapis.com/customsearch/v1?q=%s&key=%s&cx=%s&image_url=%s)"

def imgsearch(url=TEST_URL, res_count=102):
    start = 0
    dump = []
    full_query = urllib.parse.quote(QUERY % "")
    #print(full_query)
    while start < res_count:
        req_url = BASE % (full_query, API_KEY, CX, url)
        if start != 0: req_url += "&start=" + str(start)
        #print(req_url)
        resp = requests.get(req_url)
        # json comes back looking like this, looks and works just like a python dictionary
        # {
        #   "items": [
        #      "link": "XXXXX",
        #   ]
        # }
        res = resp.json()
        #print(res)
        try:
            dump.append([ i["link"] for i in res["items"] ]) # so we parse the data like this
            start = res["queries"]["nextPage"][0]["startIndex"]
        except KeyError:
            break
    return dump



# we'll just output this by running "py imgsearch.py"
if __name__ == "__main__":
    print(imgsearch())
