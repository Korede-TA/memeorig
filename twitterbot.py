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
image_tweet = []

#mybot = api.get_user(Screen_name = '@_DreamTeamBot')
for tweet in tweepy.Cursor(api.search, q = '#cat', since = '2018-03-23', until = '2018-03-24', lang = "en").items():
    for media in tweet.entities.get("media",[{}]):
        if media.get("type", None) == "photo":

            image_tweet.append({'url':tweet.entities['media'][0]['media_url'], 'id':tweet.id})
            print image_tweet
            try:
                print("\n")
                print("Found tweet by: @" + tweet.user.screen_name)

                if (tweet.retweeted == False):
                    tweet.retweet()
                    print("Retweeted the tweet")
                else:
                    print("Already retweeted the tweet")
                if (tweet.favorited == False):
                    tweet.favorite()
                    print("Favorited the tweet")
                else:
                    print("Already favorited the tweet")
                if tweet.user.following == False:
                    tweet.user.follow()
                    print("Followed the user")
                else:
                    print("Already Following the user")

            except tweepy.TweepError as e:
                    print (e.reason)
                    #time.sleep(10)
                    continue

            except StopIteration:
                break






