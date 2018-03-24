import os
import tweepy
import time
import datetime
from flask import Flask

consumerKey = 'TNRHGsKZ9eLFicSVp0mYz8jES'
consumerSecret = 'pAJME2uhBnc3cJlcTsFfNLtnoPWos0l9YiRLhiNxJxBGtH1YlR'
accessToken = '977428488398483456-IpIS5IqEsVJRGyrqoWOBom9AlKVg6WL'
accessTokenSecret = 'NkMVr8B0g7ehSQNbX8WUOymTIuN7wFng5CAQe4QMZR1ox'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

auth.secure = True
api = tweepy.API(auth)

today = datetime.date.today()
duration = datetime.timedelta(days=7)

#mybot = api.get_user(Screen_name = '@_DreamTeamBot')
bothandle = "swag_ebby"

def on_mention_reply():
    q = "to:%s" % bothandle
    last_status_var = "MEMEORIG_LAST_STATUS"
    res = tweepy.search(q, since_id=os.environ[last_status_var]) if os.environ.has_key(last_status_var) else tweepy.search(q)

    for tweet in res:
        ## reply text would usually be the earliest tweet with the image
        reply_text = "http://twitter.com/jack/status/20"
        api.update_status(reply_text, in_reply_to_status_id = tweet.id)

def on_mention_compare():
    q = "to:%s compare" % bothandle
    last_status_var = "MEMEORIG_LAST_STATUS"
    res = tweepy.search(q) 
    for tweet in res:
        media = tweet.entities.get("media", [{}])
        similarity_score = imgcomp(media[0]['medial_url'], media[1]['medial_url'])
        reply_text = "image similarity: " + str(similarity_score*100)
        api.update_status(reply_text, in_reply_to_status_id = tweet.id)
    
if __name__ == "__main__":
    while True:
        try:
            on_mention_reply()
            on_mention_compare()
            time.sleep(100)
        except:
            break
