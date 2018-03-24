import re
from mrjob.job import MRJob
from imgsearch import imgsearch
from imgcomp import imgcomp
import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class TwitImgSimilarity(MRJob):
    pass

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

def process():
    root_img = "https://pbs.twimg.com/media/DXpdVIFVwAA0Bsx.jpg"
    res = imgsearch(root_img)
    for i in res:
        print(imgcomp(root_img, i))

if __name__ == "__main__":
    process()
