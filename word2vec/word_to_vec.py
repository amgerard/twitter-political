import tweepy
import re
import enchant
import json
import gensim, logging

english_words = enchant.Dict("en_US")

def is_canidate(x):
	return re.match('hillary',x) or re.match('trump',x)

def get_words(mystr):
	tokens = re.sub("[^\w]", " ",  mystr).split()
	words =  [x for x in tokens if english_words.check(x) or is_canidate(x)]
	return words

def split_into_sentences(pathToData):
sentences = []
# with open('~/Research/Data/Twitter/HILLARY2016.txt') as f:
with open(pathToData) as f:
	for line in f.readlines():
		d = json.loads(line) # pass
		if 'text' in d:
			sentences.append(get_words(d['text']))

def create_model(sentences):
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
 	# train word2vec
	model = gensim.models.Word2Vec(sentences, min_count=1)

# ------------------------------------
# Run it all
datafile = '/Volumes/HD02/Users/John/Research/Data/Twitter/HILLARY2016.txt'
split_sentences = split_into_sentences(datafile)
model = create_model(split_sentences)

# Save the model to disk
fname = "word2vecModel"
model.save(fname)


#print model.similar_by_word('trump', topn=100)
#print model.most_similar();
#print model.similarity('hilary', 'suck')
#print model.similarity('trump', 'bad')
#print model.doesnt_match("Hillary happy hate crooked".split())

