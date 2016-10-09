from load_json_file import load_json_file
import get_tweet_info as gt
import numpy as np
import matplotlib.pyplot as plt


def plot_tweet_locations(locs1,locs2=[]):
	plt.plot(locs1[:,1],locs1[:,0],'b.')

	if locs2!=[]:
		plt.plot(locs2[:,1],locs2[:,0],'r.')
	
	plt.xlabel('Latitude')
	plt.ylabel('Longitude')
	# plt.xlim([-140, -55]) # Center on American
	# plt.ylim([15, 60])
	plt.show()

# --------------------------------------------------
# Here's how you use it:
pathToHill  = '/Volumes/HD02/Users/John/Research/Data/Twitter/HILLARY2016.txt'
pathToTrump = '/Volumes/HD02/Users/John/Research/Data/Twitter/TRUMP2016.txt'
pathToMatt = '/Volumes/HD02/Users/John/Research/Data/Twitter/Hurricane_copy.txt'

hill_objs  = load_json_file(pathToHill, 100000)
trump_objs = load_json_file(pathToTrump,100000)
matt_objs  = load_json_file(pathToMatt, 100000)

h_tweets, h_words, h_users, h_places, h_coords = read_tweets(hill_objs)
t_tweets, t_words, t_users, t_places, t_coords = read_tweets(trump_objs)
m_tweets, m_words, m_users, m_places, m_coords = read_tweets(matt_objs)

# Convert coords to numpy array
h_locs = np.asarray(h_coords)
t_locs = np.asarray(t_coords)
m_locs = np.asarray(m_coords)

# Do the plotting
plot_tweet_locations(h_latlong,t_latlong)