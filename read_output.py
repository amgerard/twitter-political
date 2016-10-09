import json
import Tweet
import pandas as pd

list_of_tweets = []
list_of_words = []
hillary_excluded_words = ['imwithher','hillaryclinton','clinton2016','#imwithher','#hillaryclinton','#clinton2016']
trump_excluded_words = ['trump2016','TrumpPence16', '#trump2016','#TrumpPence16']

excluded_words = ['imwithher','hillaryclinton','clinton2016','#imwithher','#hillaryclinton','#clinton2016',
                  'trump2016', 'TrumpPence16', '#trump2016', '#TrumpPence16', 'a','an','the','another',
                  'for','but','or','so','yet','to','you','is','of','in','are','on','and','I']

## COMMENT AND UNCOMMENT AS NEEDED BELOW

###############################
data_file = 'data/TRUMP2016.txt'
outfile = open('data/trump_tweets.txt', 'w', encoding=('utf-8'))

# data_file = 'data/HILLARY2016.txt'
# outfile = open('data/hillary_tweets.txt', 'w', encoding=('utf-8'))

# data_file = 'data/test_TRUMP.txt'
# outfile = open('data/test_trump_tweets.txt', 'w', encoding=('utf-8'))

#########################

counter = 0
file = open(data_file, 'r')
# outfile = open('tweets.tab', 'w')

line = file.readline()

# loop line by line
while line != "":
    if line == '\n':
        line = file.readline()
        continue
        # turn line into json object
    try:
        JSON_line = json.loads(line)
    except:
        line = file.readline()
        continue

    # Pull out tweet status
    try:
        text = JSON_line['text']
        # remove if a obvious RT
        if text.startswith('RT'):
            print("dumped retweet")
            line = file.readline()
            continue
    except:
        line=file.readline()
        continue
    # clean out URLS and hashtags we collected with
    text = text.split()
    for word in text:
        lower_word = word.lower()
        if lower_word.startswith('http'):
            text.remove(word)
        if lower_word in excluded_words:
            text.remove(word)
            print('removed: ' + word)
        list_of_words.append(word)
    text = ' '.join(text)
    outfile.write(text + '\n')


    # user = JSON_line['user']['name']

    # put into dict, this makes for easy conversion to DataFrame
    # tweet = {'status':text, 'user':user}
    #
    # list_of_tweets.append(tweet)
    # line = file.readline()

file.close()
outfile.close()



