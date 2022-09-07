
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
											max_results = numtweet
											,user_fields=['username'],
											expansions=['author_id'])
	# db = pd.json_normalize(tweets[1])
	# dc = pd.json_normalize(tweets)
	# dc.to_json('test.json')
	username = []
	text = []
	for tweet in tweets[0]:
		text.append(tweet.text)
		# print(tweet.text)
	for user in tweets[1]['users']:
		username.append(user.username)
		# print(user.username)

	a =	{'username': username,'text' : text}
	dd = pd.DataFrame.from_dict(a,orient='index')
	dd = dd.transpose()
	filename = 'tweets.csv'
	dd.to_csv(filename)


def main():
	start_time = datetime.datetime.now() - datetime.timedelta(days=2)
	end_time = datetime.datetime.now() - datetime.timedelta(days=1)
	numtweet = 100
	# print(start_time, end_time)
	client_scrape(u"(#طنز OR #خنده OR #جوک OR #کمدی OR #خنده_دار OR 😂 😂 😂 ) lang:fa -is:retweet -is:reply", start_time,end_time, numtweet)
	# print('Scraping has completed!')

if __name__ == '__main__':
	main()

