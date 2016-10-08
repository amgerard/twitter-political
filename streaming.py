import tweepy
import json
## API KEYS
consumer_key = 'NDhA67vWwE6dj2rmAiKAIkYEk'
consumer_secret = 'XZVpin5MVw5Y1hWWZCLbQr483GqN7GZlzDs28dZH4XQyeIxrw9'
access_key = '324669819-12jthC7lkuuKz9t1hOp6BtejTmeG0eJa6oTP2b4Q'
access_secret = 'tSwvVT0rJ56vGmVCoQ0YxKndvEB09uXlSZA54Fr5RhYhX'

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
