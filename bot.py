import os
import datetime
import random
import tweepy
import time
import datetime
from flask import Flask
from imgcomp import imgcomp

# consumerKey = 'TNRHGsKZ9eLFicSVp0mYz8jES'
consumerKey = '3BjzqJeIhSX3xO34lOT2k14ss'
# consumerSecret = 'pAJME2uhBnc3cJlcTsFfNLtnoPWos0l9YiRLhiNxJxBGtH1YlR'
consumerSecret = 'iHNthqrA0MYa91G6obnSVe3lrtke4kc5x2X9rLa9LrwoT1TJqj'
# accessToken = '977428488398483456-IpIS5IqEsVJRGyrqoWOBom9AlKVg6WL'
accessToken = '1319165414-amcgiPJCwifYXJQPqrIADJCO9SGF8Ocwpr66XUF'
# accessTokenSecret = 'NkMVr8B0g7ehSQNbX8WUOymTIuN7wFng5CAQe4QMZR1ox'
accessTokenSecret = 'th7kEIbWWkzqN8BIiu5RMU27cVdg0R0re4ZZleih462mH'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

auth.secure = True
api = tweepy.API(auth)

today = datetime.date.today()
duration = datetime.timedelta(days=7)

#mybot = api.get_user(Screen_name = '@_DreamTeamBot')
bothandle = "swag_ebby"

random.seed(datetime.datetime.now())

def on_mention_reply():
    q = "to:%s" % bothandle
    last_status_var = "MEMEORIG_LAST_STATUS"
    res = api.search(q, since_id=os.environ[last_status_var]) if last_status_var in os.environ else api.search(q)

    for tweet in res:
        ## reply text would usually be the earliest tweet with the image
        reply_text = "http://twitter.com/jack/status/20"
        api.update_status(reply_text, in_reply_to_status_id = tweet.id)

def status_media_url(status):
    media = status.entities.get("media", [])
    return media[0]['media_url']

def on_mention_compare():
    q = "to:%s compare" % bothandle
    res = api.search(q) 
    for tweet in res:
        print(tweet.id)
        print(tweet.text)
        print(tweet.entities['media'])
        last_status_var = "MEMEORIG_LAST_STATUS"
        media = tweet.entities.get("media", [{}])
        url1 = status_media_url(tweet)
        url2 = status_media_url(api.get_status(tweet.in_reply_to_status_id))
        if len(media) == 2:
            similarity_score = imgcomp(url1, url2)
            reply_text = "image similarity: " + str(similarity_score*100) + "%"
        else:
            reply_text = "put in two images to compare image"
        reply_text += " #" + str(random.randint(1,100))
        print(reply_text)
        api.update_status(reply_text, in_reply_to_status_id = tweet.id)
    
if __name__ == "__main__":
    while True:
        try:
            #on_mention_reply()
            on_mention_compare()
            time.sleep(10)
        except tweepy.error.TweepError as e:
            print(e)
            print('duplicate')
            continue
        except Exception as e:
            print(e)
            break
