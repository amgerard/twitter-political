import tweepy
import re
import enchant
import json

english_words = enchant.Dict("en_US")

def is_canidate(x):
	return re.match('hilary',x) or re.match('trump',x)

def get_words(mystr):
	tokens = re.sub("[^\w]", " ",  mystr).split()
	words =  [x for x in tokens if english_words.check(x) or is_canidate(x)]
	return words

sentences = []
with open('data/Backup_HILLARY2016.txt') as f:
	for line in f.readlines():
		d = json.loads(line) # pass
		if 'text' in d:
			sentences.append(get_words(d['text']))

print len(sentences)

# import modules & set up logging
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
 
# train word2vec
model = gensim.models.Word2Vec(sentences, min_count=1)
print model['trump']
#print model.similar_by_word('trump', topn=100)
#print model.most_similar();
#print model.similarity('hilary', 'suck')
#print model.similarity('trump', 'bad')
