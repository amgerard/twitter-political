from textblob import TextBlob

def measure_sentiment(list_of_tweets):
    hillary_sentences = []
    trump_sentences = []

    tweets_str = ' '.join(list_of_tweets)
    blob = TextBlob(tweets_str)

    for sentence in blob.sentences:
        sent = sentence.string
        if sent.__contains__("Donald" or "donald" or "Trump" or "trump"):
            trump_sentences.append(sentence)
        if sent.__contains__("Hillary" or "hillary" or "Clinton" or "clinton"):
            hillary_sentences.append(sentence)

    trump_pol = 0
    trump_pol_list = []
    for sentence in trump_sentences:
        # print(sentence.string)
        # print(sentence.sentiment)
        if sentence.sentiment.polarity != 0:
            trump_pol += sentence.sentiment.polarity
            trump_pol_list.append(sentence.sentiment.polarity)

    # print('*************************')
    # print('*************************')

    hill_pol = 0
    hill_pol_list = []
    for sentence in hillary_sentences:
        # print(sentence.string)
        # print(sentence.sentiment)
        if sentence.sentiment.polarity != 0:
            hill_pol += sentence.sentiment.polarity
            hill_pol_list.append(sentence.sentiment.polarity)

    try:
        t_sentiment = trump_pol / len(trump_pol_list)
    except:
        t_sentiment = "NOT ENOUGH DATA"
    try:
        h_sentiment = hill_pol / len(hill_pol_list)
    except:
        h_sentiment = "NOT ENOUGH DATA"

    # print("Trump sentiment: " + str(t_sentiment))
    # print("Clinton sentiment: " + str(h_sentiment))

    return {'hillary_sentiment': h_sentiment, 'trump_sentiment':t_sentiment, 'trump_list': trump_pol_list, 'hillary_list':hill_pol_list}


def sentiment_over_time(tweets_with_date):
    from Tweet import TweetSentiment
    hillary_sentences = []
    trump_sentences = []
    tweet_sentiments = []

    for i in range(0, len(tweets_with_date)):
        blob = TextBlob(tweets_with_date[i].status)

        for sentence in blob.sentences:

            if sentence.string.__contains__("Hillary" or "hillary" or "Clinton" or "clinton"):
                hillary_sentences.append(sentence)
            if sentence.string.__contains__("Donald" or "donald" or "Trump" or "trump"):
                trump_sentences.append(sentence)

            polarity = sentence.sentiment.polarity
            if polarity != 0:
                TweetSentiment(sentiment=polarity, timeinfo=tweets_with_date[i].timeinfo)
                tweet_sentiments.append(TweetSentiment)

    return tweet_sentiments




