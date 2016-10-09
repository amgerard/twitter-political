from flask import Flask, render_template, request
from user_crawler.get_user_tweets import get_user_tweets, get_tweets_with_time
from sentiment_analysis.sentiment import measure_sentiment, measure_sentiment_over_time
from sentiment_analysis.plotting import generate_heatmap
import time
from Tweet import Tweet

import tempfile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('input.html', title="Tweet Sentiment Analyzer")



@app.route('/submit', methods=['POST'])
def submit():
    # get username from input
    username = request.form['twitter_name']
    tweets = get_user_tweets(username)
    results = measure_sentiment(tweets)
    t_sent = results['trump_sentiment']
    h_sent = results['hillary_sentiment']

    ## GENERATE PLOT HERE AND RETURN IT IN A NEW TEMPLATE
    h_plotPng = generate_heatmap(results['hillary_list'], "Hillary Sentiment")
    time.sleep(0.5)
    t_plotPng = generate_heatmap(results['trump_list'], "Trump Sentiment")

    del(results)
    del(tweets)

    # sentiment over time
    tweets = get_tweets_with_time(username)
    lineplot = measure_sentiment_over_time(tweets, twitterHandle=username)
    del tweets

    return render_template('output.html', username=username, hillary_sentiment = h_sent, trump_sentiment = t_sent,
                           h_plotPng=h_plotPng, t_plotPng = t_plotPng, title="@" + username, lineplot = lineplot)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
