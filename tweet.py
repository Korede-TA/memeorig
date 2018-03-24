import tweepy
import time
import datetime

consumerKey = 'IZKJ61V9aLa594A1Zhm4rVw2F'
consumerSecret = 'P1ov6Nw20TLdy0kprlQv075GbCeG4ChG9twTsCszooAnsXE6UL'
accessToken = '788286853-Gzi5Jqkyd6amQAteDQP63EVbFvx75MIEduK7Jyrb'
accessTokenSecret = 'T1CVwTwMJIuSJcZzbi7rhl5P0V2Z5Jftwtf5K6K2hPAK7'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

auth.secure = True
api = tweepy.API(auth)


#mybot = api.get_user(Screen_name = '@_DreamTeamBot')
def getimg(query):
    img_urls = []
    for tweet in tweepy.Cursor(api.search, q = query).items(1000):
        all_media = tweet.entities.get("media",[{}])
        for cont in all_media:
             if cont.get("type", None) == "photo":
             	mylist = [tweet.user.screen_name, tweet.created_at, cont['media_url']]
                img_urls.append(mylist)
    print(img_urls)
    return img_urls
    
getimg("#meme")





