
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
    results = api.user_timeline(username)

    # repeat calls until max reached
    while counter < collection_rounds:
        for i in range(0,14):
            tweets.append(results[i].text)
        results = api.user_timeline(username, max_id = results.since_id)
        counter += 1

    return tweets




