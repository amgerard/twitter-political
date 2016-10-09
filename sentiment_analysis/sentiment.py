from textblob import TextBlob
from datetime import datetime
import matplotlib.pyplot as plt

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


def measure_sentiment_over_time(tweetObjs):
    
    list_of_tweets = []
    list_of_times = []
    for n in range(0,len(tweetObjs)):
        list_of_tweets.append(tweetObjs[n].status)
        list_of_times.append(tweetObjs[n].timeinfo)
    
    hillary_sentences = []
    trump_sentences = []
    
    tweets_str = ' '.join(list_of_tweets)
    blob = TextBlob(tweets_str)
    
    # Determine which sentences are about Trump and which are about Hillary
    mask_include_trump = []
    mask_include_hill = []
    t = 0
    h = 0
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
            mask_include_trump.append(t)
        t = t + 1
    
    # print('*************************')
    # print('*************************')
    
    h = 0
    hill_pol = 0
    hill_pol_list = []
    for sentence in hillary_sentences:
        # print(sentence.string)
        # print(sentence.sentiment)
        if sentence.sentiment.polarity != 0:
            hill_pol += sentence.sentiment.polarity
            hill_pol_list.append(sentence.sentiment.polarity)
            mask_include_hill.append(h)
        h = h + 1

    # Use the masks from above to cut out the dates from the tweets we want
    times_trump  = [list_of_times[ mask_include_trump[idx]] for idx in range(0, len(mask_include_trump))]
    tweets_trump = [list_of_tweets[mask_include_trump[idx]] for idx in range(0, len(mask_include_trump))]
    times_hill   = [list_of_times[ mask_include_hill[idx]]  for idx in range(0, len(mask_include_hill))]
    tweets_hill  = [list_of_tweets[mask_include_hill[idx]]  for idx in range(0, len(mask_include_hill))]
    
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

    # ------------------------------------------
    # Do the plotting
    
    t_trump = [(t - min(times_trump)).total_seconds()/60/60 for t in times_trump]
    t_hill  = [(t - min(times_hill )).total_seconds()/60/60 for t in times_hill]
    plt.plot(t_trump,trump_pol_list,'ro-')
    plt.plot(t_hill,hill_pol_list,'bo-')
    plt.xlabel('Hours since first tweet')
    plt.ylabel('Polarity list')
    plt.ylim([-1.5, 1.5])
    plt.show()
    

    return {'hillary_sentiment': h_sentiment, 'trump_sentiment': t_sentiment, 'trump_list': trump_pol_list,
            'hillary_list': hill_pol_list, 'hillary_times': times_hill, 'trump_times': times_trump,
            'trump_tweets':tweets_trump,'hillary_tweets':tweets_hill}
    