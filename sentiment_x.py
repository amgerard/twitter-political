#from nltk.classify import NaiveBayesClassifier
#from nltk.corpus import subjectivity
#from nltk.sentiment import SentimentAnalyzer
#from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#import nltk
import json
import re
import enchant
# note: use download to get vader_lexicon.txt
#nltk.download()

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
        return re.match('hillary',x) or re.match('trump',x)

def get_words(mystr):
        tokens = re.sub("[^\w]", " ",  mystr).split()
        words =  [x for x in tokens if english_words.check(x)] #  or is_canidate(x)]
        return words

tweets = []
for filename in ('data/Backup_HILLARY2016.txt','data/TRUMP2016.txt'):
        with open(filename) as f:
                for line in f.readlines():
                        d = json.loads(line) # pass
                        if 'text' in d:
                                tweets.append(' '.join(get_words(d['text'])))
                print 'test: ' + str(len(tweets))

sid = SentimentIntensityAnalyzer()
pos_hil = 0
neg_hil = 0
pos_don = 0
neg_don = 0
cnt = 0
for tweet in tweets:
	ss = sid.polarity_scores(tweet)
	#print ''
	#print tweet
	#for k in sorted(ss):
	#	print('{0}: {1}, '.format(k, ss[k]))
	if cnt < 32929:
		pos_hil = pos_hil + ss['pos']
		neg_hil = neg_hil + ss['neg']
	else:
		pos_don = pos_don + ss['pos']
		neg_don = neg_don + ss['neg']
	cnt = cnt + 1

print 'total positive = ' + str(pos_hil + pos_don)
print 'total negative = ' + str(neg_hil + neg_don)
print 'hillary positive = ' + str(pos_hil)
print 'hillary negative = ' + str(neg_hil)
print 'donald positive = ' + str(pos_don)
print 'donald negative = ' + str(neg_don)

# another example
'''
n_instances = 100
subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]

train_subj_docs = subj_docs[:80]
test_subj_docs = subj_docs[80:100]
train_obj_docs = obj_docs[:80]
test_obj_docs = obj_docs[80:100]
training_docs = train_subj_docs+train_obj_docs
testing_docs = test_subj_docs+test_obj_docs

sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)
for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
	print('{0}: {1}'.format(key, value))
'''
