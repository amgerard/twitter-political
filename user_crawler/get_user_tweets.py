
def get_user_tweets(username, collection_rounds = 5):
    import tweepy
    from user_crawler import secrets

    ## API KEYS
    consumer_key = secrets.consumer_key
    consumer_secret = secrets.consumer_secret
    access_key = secrets.access_key
    access_secret = secrets.access_secret

    ## Set up Auth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    tweets = []
    counter = 0

    # get the first results
    results = api.user_timeline(username, count=200, include_rts=1)

    # repeat calls until max reached
    while counter < collection_rounds:
        for i in range(0,len(results)):
            tweets.append(results[i].text)
        results = api.user_timeline(username, max_id = results.max_id, count=200, include_rts=1)
        counter += 1

    return tweets


def get_tweets_with_time(username, collection_rounds = 5):

    import tweepy
    from user_crawler import secrets
    from Tweet import Tweet

    ## API KEYS
    consumer_key = secrets.consumer_key
    consumer_secret = secrets.consumer_secret
    access_key = secrets.access_key
    access_secret = secrets.access_secret

    ## Set up Auth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    results = api.user_timeline(username, count=200, include_rts=1)
    counter = 0
    tweets = []

    # repeat calls until max reached
    while counter < collection_rounds:
        for i in range(0,len(results)):
            tweet = Tweet(status=results[i].text, timeinfo=results[i].created_at)
            tweets.append(tweet)
        results = api.user_timeline(username, max_id = results.max_id, count=200, include_rts=1)
        counter += 1

    return tweets



