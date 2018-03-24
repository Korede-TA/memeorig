import tweepy
import time
import datetime

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
def getimg(query):
    img_urls = []
    for tweet in tweepy.Cursor(api.search, q = query).items(1000):
        all_media = tweet.entities.get("media",[{}])
        for cont in all_media:
             if cont.get("type", None) == "photo":
             	mylist = [tweet.user.screen_name, cont['media_url']]
                img_urls.extend(mylist)
    print(img_urls)
    return img_urls
    
getimg("#meme")





