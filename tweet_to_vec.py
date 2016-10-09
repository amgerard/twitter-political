import tweepy
import re
import enchant
import json
import numpy as np
import pandas as pd

english_words = enchant.Dict("en_US")

def makeFeatureVec(words, model, num_features):
    featureVec = np.zeros((num_features,),dtype="float32")
    nwords = 0.
    index2word_set = set(model.index2word)
    for word in words:
        if word in index2word_set: 
            nwords = nwords + 1.
            featureVec = np.add(featureVec,model[word])
    featureVec = np.divide(featureVec,nwords)
    return featureVec

def is_canidate(x):
	return re.match('hilary',x) or re.match('trump',x)

def get_words(mystr):
	tokens = re.sub("[^\w]", " ",  mystr).split()
	words =  [x for x in tokens if english_words.check(x) or is_canidate(x)]
	return words

tweets = []
with open('data/Backup_HILLARY2016.txt') as f:
	for line in f.readlines():
		d = json.loads(line) # pass
		if 'text' in d:
			tweets.append(get_words(d['text']))

print len(tweets)

# import modules & set up logging
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
 
# train word2vec
model = gensim.models.Word2Vec(tweets, min_count=1)
#print model['trump']
#print model.similar_by_word('trump', topn=100)
#print model.most_similar();
#print model.similarity('hilary', 'suck')
#print model.similarity('trump', 'bad')

dummy_cols = [str(x) for x in range(1,101)]
#tweet_vecs = pd.DataFrame(index=np.arange(0, len(tweets)), columns=dummy_cols)
tweet_vectors = [] # np.empty((len(tweets),100), float)
for i in range(len(tweets)):
	tweet = tweets[i]
	#np.append(tweet_vectors, makeFeatureVec(tweet, model, 100), axis=0)
	vec = makeFeatureVec(tweet, model, 100)
	if vec.shape[0] == 100:
		#np.append(tweet_vectors, vec, axis=0)
		tweet_vectors.append(vec)
		#tweet_vecs.loc[i] = vec
	else:
		print 'weird'

print 'done'
tweet_vecs = pd.DataFrame(tweet_vectors)
print tweet_vecs.shape	

