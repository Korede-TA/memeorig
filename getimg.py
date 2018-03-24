import requests

URL = "https://stream.twitter.com/1.1/statuses/filter.json"
PARAMS = { q : "%s OR %s OR %s filter:images"}
result = requests.get(url = URL, params = PARAMS)
data = result.json()