import tweepy
import re
import enchant
import json
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

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
				tweets.append(get_words(d['text']))
		print 'test: ' + str(len(tweets))

print len(tweets)

# import modules & set up logging
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
 
# train word2vec
ndim = 200
model = gensim.models.Word2Vec(tweets, min_count=1, size=ndim)
#print model['trump']
#print model.similar_by_word('trump', topn=100)
#print model.most_similar();
#print model.similarity('hilary', 'suck')
#print model.similarity('trump', 'bad')

#dummy_cols = [str(x) for x in range(1,101)]
#tweet_vecs = pd.DataFrame(index=np.arange(0, len(tweets)), columns=dummy_cols)
tweet_vectors = [] # np.empty((len(tweets),100), float)
for i in range(len(tweets)):
	tweet = tweets[i]
	#np.append(tweet_vectors, makeFeatureVec(tweet, model, 100), axis=0)
	vec = makeFeatureVec(tweet, model, ndim)
	if vec.shape[0] == ndim and np.isnan(vec).any() == False:
		#np.append(tweet_vectors, vec, axis=0)
		tweet_vectors.append(vec)
		#tweet_vecs.loc[i] = vec
	else:
		print 'weird'

print 'done'
tweet_vecs = pd.DataFrame(tweet_vectors)


print tweet_vecs.shape	
'''
from sklearn import cluster
k = 10
kmeans = cluster.KMeans(n_clusters=k)
kmeans.fit(tweet_vecs)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print centroids
'''
from sklearn import decomposition

X = tweet_vecs
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)

print pca.components_.shape
print pca.explained_variance_ratio_.shape
print pca.explained_variance_ratio_

import matplotlib.pyplot as plt

fig = plt.figure()
#ax = fig.add_subplot(111)
ax = fig.add_subplot(111, projection='3d')

#x = pca.components_[0,:]
#y =pca.components_[1,:]
#z = pca.components_[2,:]

x = X[:,0]
y =X[:,1]
z = X[:,2]

#plt.plot(x[:1000],y[:1000], marker='o', color='b', markersize=3)
#plt.plot(x[:32952],y[:32952], marker='o', color='b', markersize=3)
#plt.plot(x[32952:33952],y[32952:33952], marker='o', color='r', markersize=3)
#plt.plot(x[32952:],y[32952:], marker='o', color='r', markersize=3)

ax.scatter(x[:1000],y[:1000],z[:1000], marker='o', color='b')
ax.scatter(x[32952:33952],y[32952:33952],z[32952:33952], marker='o', color='r')

#ax.scatter(x, y, c='r', marker='o')
#ax.set_xlabel('X Label')
#ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')

plt.show()



