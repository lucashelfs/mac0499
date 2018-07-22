import tweepy
import json
import time

# Dados do app no twitter
from consumer_secret import *


class CollectorListener(tweepy.StreamListener):

	filename = '../dados/presidenciaveis-' + time.strftime("%d-%m-%Y") + '.json'

	def on_data(self, data):

		tweet = json.loads(data)

		if not tweet['retweeted'] and 'RT @' not in tweet['text']:
			with open(self.filename, 'a') as f:
				f.write(data)

		def on_error(self, status):
			print('Erro! Código: ', status)

		def abre_coletados(filename):
			tweets = []
			for line in open(filename, 'r'):
				tweets.append(json.loads(line))
				return tweets

if __name__ == '__main__':

	listener = CollectorListener()
	print('Coletando tweets contendo os candidatos a presidência...')

	# Autentica
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	# Connecta na API
	stream = tweepy.Stream(auth, listener)
	stream.filter(track=['Lula', 'Bolsonaro', 'Marina Silva', 'Ciro Gomes', 'Geraldo Alckmin'])
