class Tweet:

    def __init__(self, status, timeinfo):
        self.status = status
        self.timeinfo = timeinfo


class TweetSentiment:

    def __init__(self, sentiment, timeinfo, subject):
        self.sentiment = sentiment
        self.timeinfo = timeinfo
        self.subject = subject
