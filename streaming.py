import tweepy
import json
## API KEYS
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''

## Set up Auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#####
#EDIT OUTPUT DIR BELOW
####
output = open('data/TRUMP2016.txt', 'w')


class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        print(data)
        output.write(data)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener= myStreamListener)


## EDIT SEARCH PHRASE BELOW
myStream.filter(track=['trump2016'])
