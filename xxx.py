
from numpy import result_type
import pandas as pd
import tweepy
import configparser
import datetime
from tweepy import Client
# import jsonpickle
# from json import dump, encoder

bearer_token = "AAAAAAAAAAAAAAAAAAAAAFaBbgEAAAAA8DXS4QTGwcTFfew0G3qNSVaokwA%3DOZ9WWcNNQ7VtmbFN5MikeZDIget4PBcqFnouiivhxlVq3BnwGc"
consumer_key = "sdrLvjrFdmisIF4xcZClmUr09"
consumer_secret = "ZVM2EsN2q1BGWhpSejP70VfsHUHyWmp7CgZxZHaHGZSqky0OCz"
access_token = "1516026377421602818-3hjmbHz0G0TcqwOLMJ7p76Vu9ndVyP"
access_token_secret= "y5ER3YBvGbBsCkqrmvr51UePas59CP2s6rPOwkreGPSoT"


client = tweepy.Client(bearer_token,consumer_key,consumer_secret,access_token,access_token_secret)


def client_scrape(words, start_time, end_time, numtweet):
	tweets = client.search_recent_tweets(query=words,start_time=start_time,end_time=end_time,
											max_results = numtweet,tweet_fields=['public_metrics']
											,user_fields=['username'],
											expansions=['author_id'])
	# db = pd.json_normalize(tweets[1])
	# dc = pd.json_normalize(tweets)
	# dc.to_json('test.json')
	username = []
	text = []
	likes = []
	for tweet in tweets[0]:
		text.append(tweet.text)
		likes.append(tweet.public_metrics.like_count)
	for user in tweets[1]['users']:
		username.append(user.username)
	
	# for metrics in tweets[0]:
	# 	likes.append(metrics.public_metrics.like_count)
		# print(user.username)
	# tweets0DF = pd.DataFrame(tweets[0])
	# tweets1DF = pd.DataFrame(tweets[1])
	# tweets0DF.to_json('test.json')
	# tweets1DF.to_json('test2.json')
	# tweets_test = pd.DataFrame(tweets[2])
	# tweets_test.to_json('test3.json')
	########
	a =	{'username': username,'text' : text, 'likes':likes}
	dd = pd.DataFrame.from_dict(a,orient='index')
	dd = dd.transpose()
	filename = 'tweets.csv'
	test = dd.sort_values(by='likes', ascending=False)
	test.to_csv(filename)


def main():
	start_time = datetime.datetime.utcnow() - datetime.timedelta(hours=2) 
	end_time = datetime.datetime.utcnow() - datetime.timedelta(seconds=15)
	numtweet = 100
	# print(start_time, end_time)
	client_scrape(u"(#طنز OR #خنده OR #جوک OR #کمدی OR 😂 😂 😂  OR #خنده_دار) lang:fa -is:retweet -is:reply", start_time,end_time, numtweet)
	# print('Scraping has completed!')

if __name__ == '__main__':
	main()

